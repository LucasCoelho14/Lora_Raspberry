import spidev
import RPi.GPIO as GPIO
import time

# Configuração dos pinos SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # Barramento SPI 0, dispositivo 0

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