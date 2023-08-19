import spidev
import RPi.GPIO as GPIO
import time

# Configuração dos pinos SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # Barramento SPI 0, dispositivo 0

<<<<<<< HEAD
# Configuração dos pinos GPIO para LoRa
cs_pin = 8       # GPIO8 - NSS
reset_pin = 22   # GPIO22 - NRESET
dio0_pin = 4     # GPIO4 - DIO0

# Inicialização dos pinos GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(cs_pin, GPIO.OUT)
GPIO.setup(reset_pin, GPIO.OUT)
GPIO.setup(dio0_pin, GPIO.IN)

def check_lora_connection():
    try:
        # Configuração para realizar a leitura do registrador de versão (pode variar de acordo com o módulo LoRa)
        read_version_cmd = [0x42, 0x00]

        # Seleciona o dispositivo LoRa no barramento SPI
        GPIO.output(cs_pin, GPIO.LOW)

        # Envia o comando de leitura do registrador
        spi.xfer(read_version_cmd)

        # Deseleciona o dispositivo LoRa
        GPIO.output(cs_pin, GPIO.HIGH)

        # Retorne True se não houver exceções
        return True
    except:
        return False

try:
    if check_lora_connection():
        print("Módulo LoRa está conectado e respondendo!")
    else:
        print("Não foi possível verificar a conexão com o módulo LoRa.")
        
except KeyboardInterrupt:
    pass

finally:
    spi.close()  # Feche a comunicação SPI
    GPIO.cleanup()  # Limpeza dos pinos GPIO
=======
#defina a função de setar a frequencia do Lora
def set_freq(f):
        i = int(f * 16384.)    # choose floor
        msb = i // 65536
        i -= msb * 65536
        mid = i // 256
        i -= mid * 256
        lsb = i
        return Lora.xfer([ 0x06 | 0x80, msb, mid, lsb])
#Constantes que representam o modo de operação
SLEEP    = 0x80
STDBY    = 0x81
FSTX     = 0x82
TX       = 0x83
FSRX     = 0x84
RXCONT   = 0x85
RXSINGLE = 0x86
CAD      = 0x87
FSK_STDBY= 0x01
Lora = spidev.SpiDev()
Lora.open(0,0)
set_freq(915.0)
Lora.xfer2([(0x01| STDBY)])
Lora.xfer2([0x0E | 0x80, localtxaddr])
Lora.xfer2([(fifoptraddr) | 0x80, localtxaddr])
while True:
    dados = "oi, esp32"
    payload = bytes(dados, 'utf-8')
    payload_length = [len(payload)]
    Lora.xfer2([0xBC])
    Lora.xfer([localtxaddr])
    Lora.xfer2(payload_length)
    Lora.xfer2(payload)
    Lora.xfer2([(0x01)&0x7F | 0x83])
    print("Enviando...\n")
    time.sleep(2)
>>>>>>> 734853292e8850781978dd7a772f70854207f4d6
