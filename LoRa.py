from pyLoRa import LoRa
import time

# Configuração dos pinos GPIO para LoRa
cs_pin = 8      # GPIO8 - NSS
reset_pin = 22  # GPIO22 - NRESET
dio0_pin = 4    # GPIO4 - DIO0

# Inicialização do módulo LoRa
lora = LoRa(cs_pin, reset_pin, dio0_pin)

try:
    if lora.begin(freq=915E6):
        print("Módulo LoRa está conectado!")
        
        # Mensagem a ser enviada
        message = "Oi ESP32!"

        # Envia a mensagem
        lora.send_data(message)
        print(f"Mensagem enviada: {message}")

    else:
        print("Não foi possível inicializar o módulo LoRa.")
        
except KeyboardInterrupt:
    pass

finally:
    lora.close()
