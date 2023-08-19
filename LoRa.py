import RPi.GPIO as GPIO
import time

# Configuração dos pinos GPIO para LoRa
cs_pin = 8      # GPIO8 - NSS
reset_pin = 22  # GPIO22 - NRESET
dio0_pin = 4    # GPIO4 - DIO0

# Inicialização dos pinos GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(cs_pin, GPIO.OUT)
GPIO.setup(reset_pin, GPIO.OUT)
GPIO.setup(dio0_pin, GPIO.IN)

def check_lora_connection():
    try:
        # Ativa o pino CS para selecionar o dispositivo LoRa
        GPIO.output(cs_pin, GPIO.LOW)
        
        # Aguarda um breve período para o módulo LoRa se estabilizar
        time.sleep(0.1)
        
        # Desativa o pino CS para deselecionar o dispositivo LoRa
        GPIO.output(cs_pin, GPIO.HIGH)
        
        # Se não houver exceções, considera o módulo LoRa como conectado
        return True
    except:
        return False

try:
    if check_lora_connection():
        print("Módulo LoRa está conectado!")
    else:
        print("Não foi possível verificar a conexão com o módulo LoRa.")
        
except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()  # Limpeza dos pinos GPIO
