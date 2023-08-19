from sx127x import SX127x
from sx127x.lib import config
from sx127x.lib.rpi import GPIO
import time

class LoRaSender(SX127x):
    def __init__(self, parameters, verbose=False):
        super(LoRaSender, self).__init__(parameters, verbose)
        
    def send(self, data):
        self.set_mode('tx')
        self.write_payload(data)
        self.set_dio_mapping([0, 0, 0, 0])
        self.clear_irq_flags()
        self.send_pkt_len(len(data))
        self.set_payload_length(len(data))
        self.set_mode('tx')
        while self.get_irq_flags()['tx_done'] == 0:
            time.sleep(0.5)

GPIO.setmode(GPIO.BCM)
lora = LoRaSender(channel=0, RST=22, verbose=False)
lora.set_mode('sleep')

message = "Hello, ESP32!"
lora.send(message.encode())

lora.set_mode('sleep')
GPIO.cleanup()
