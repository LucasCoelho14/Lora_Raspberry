import time
from sx127x import SX127x
from sx127x import MODE
from sx127x.adafruit_rfm9x import RFM9x

# Configuração dos pinos SPI para o Raspberry Pi
RADIO_SCK = 11
RADIO_MOSI = 10
RADIO_MISO = 9
RADIO_CS = 8
RADIO_RST = 25
RADIO_DIO0 = 23

# Configuração do dispositivo LoRa
lora = RFM9x(RADIO_CS, RADIO_RST, RADIO_DIO0, RADIO_SCK, RADIO_MOSI, RADIO_MISO, None, None, None, 915.0)

local_address = 0xBC
msg_count = 0
destination = 0xBB
last_send_time = 0
interval = 5  # Intervalo em segundos para envio das mensagens

# Função para enviar uma mensagem LoRa
def send_message(outgoing):
    lora.set_mode(MODE.TX)
    lora.write_byte(destination)
    lora.write_byte(local_address)
    lora.write_byte(msg_count)
    lora.write_byte(len(outgoing))
    lora.write(outgoing.encode())
    lora.set_mode(MODE.RX)

try:
    while True:
        if time.time() - last_send_time > interval:
            mensagem = "Hi Supernova! :O"  # Definição da mensagem
            send_message(mensagem)
            print("Enviando:", mensagem)
            last_send_time = time.time()
        
        # Verificar se há pacote recebido
        if lora.packet_available():
            packet = lora.receive_packet()
            recipient, sender, incoming_msg_id, incoming_length, incoming = packet
            incoming = incoming.decode()
            
            # Se o destinatário não for este dispositivo ou broadcast
            if recipient != local_address and recipient != 0xFF:
                print("Esta mensagem não é para mim.")
                continue
            
            # Imprimir detalhes da mensagem recebida
            print("Recebido do dispositivo:", hex(sender))
            print("Enviado para:", hex(recipient))
            print("ID da mensagem:", incoming_msg_id)
            print("Tamanho da mensagem:", incoming_length)
            print("Mensagem:", incoming)
            print("RSSI:", lora.packet_rssi())
            print("Snr:", lora.packet_snr())
            print()
            
except KeyboardInterrupt:
    pass

finally:
    lora.set_mode(MODE.SLEEP)
    lora.cleanup()