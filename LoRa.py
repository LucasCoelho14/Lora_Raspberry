import spidev
import RPi.GPIO as GPIO
import time

# Configuração dos pinos GPIO para LoRa
cs_pin = 8      # GPIO8 - NSS
reset_pin = 22  # GPIO22 - NRESET
dio0_pin = 4    # GPIO4 - DIO0

# Inicialização do SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # Barramento SPI 0, Dispositivo 0
spi.mode = 0b00  # Modo SPI (CPOL=0, CPHA=0)

# Inicialização dos pinos GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(cs_pin, GPIO.OUT)
GPIO.setup(reset_pin, GPIO.OUT)
GPIO.setup(dio0_pin, GPIO.IN)

def send_lora_message(message):
    # Configurações para enviar a mensagem LoRa
    GPIO.output(cs_pin, GPIO.LOW)
    # Configurações de SPI para enviar a mensagem
    # ...
    # Envio da mensagem via SPI
    # ...
    GPIO.output(cs_pin, GPIO.HIGH)

try:
    # Enviar uma mensagem
    send_lora_message("Oi ESP32!")

except KeyboardInterrupt:
    pass

finally:
    spi.close()
    GPIO.cleanup()
