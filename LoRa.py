import time
from pyLoRa import LoRa

# Configuração dos parâmetros LoRa
frequency = 915E6  # Frequência 915MHz
tx_power = 17     # Potência de transmissão (dBm)

# Inicialização do módulo LoRa
lora = LoRa(0, 0)  # Barramento SPI 0, Dispositivo 0
lora.set_mode_sleep()  # Coloca o módulo em modo sleep para configurar

lora.set_freq(frequency)
lora.set_tx_power(tx_power)
lora.set_mode_tx()  # Muda para o modo de transmissão

try:
    message = "Oi"
    
    while True:
        lora.send_packet_broadcast(message)
        print("Enviando mensagem:", message)
        time.sleep(5)  # Intervalo de envio da mensagem
except KeyboardInterrupt:
    pass

finally:
    lora.set_mode_sleep()  # Coloca o módulo de volta em modo sleep
