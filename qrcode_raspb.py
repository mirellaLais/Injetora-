from datetime import datetime
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Definição dos pinos
block_atv   = 3
lib_primer   = 2
fech_garra   = 5
vacuo        = 6
lib_ativador = 13  # Mantemos apenas o ativador
led_prod_ok  = 19
led_prod_ko  = 26

Configuração dos pinos como entrada ou saída
GPIO.setup(block_atv, GPIO.OUT)
GPIO.setup(lib_primer, GPIO.IN)
GPIO.setup(fech_garra, GPIO.OUT)
GPIO.setup(vacuo, GPIO.OUT)
GPIO.setup(lib_ativador, GPIO.OUT)  # Apenas ativador será usado
GPIO.setup(led_prod_ok, GPIO.OUT)
GPIO.setup(led_prod_ko, GPIO.OUT)

# Modelos válidos (não será usado)
# setups = ["STR07000267", "STR07000267", "STR07000267"]

# Função para validar o produto (completamente desativada)
# def validate_product(cod_produto, setup, data_e_hora):
#     return False  # Placeholder

# Inicialização (comentada pois não será usada)
# habilita = True
# if habilita:
#     GPIO.output(fech_garra, True)
#     GPIO.output(vacuo, True)
#     GPIO.output(lib_ativador, False)
#     GPIO.output(led_prod_ok, False)
#     GPIO.output(led_prod_ko, False)
#     habilita = False

# Função avenir() (não será usada)
# def avenir():
#     global habilita  
#     GPIO.output(fech_garra, True)
#     GPIO.output(vacuo, True)
#     GPIO.output(lib_ativador, True)
#     GPIO.output(led_prod_ok, True)
#     GPIO.output(led_prod_ko, True)
    
#     for n in range(5):
#         GPIO.output(led_prod_ok, True)
#         GPIO.output(led_prod_ko, True)
#         time.sleep(0.6)
#         GPIO.output(led_prod_ok, False)
#         GPIO.output(led_prod_ko, False)
#         time.sleep(0.6)

#     avenir_ = input("Digite o código Avenir: ").strip().lower()
#     indice_map = {"fxt521": 1, "fxt598": 2, "fxt551": 3}
#     if avenir_ in indice_map:
#         indice = indice_map[avenir_]
#         habilita = False
#         GPIO.output(led_prod_ok, True)
#         GPIO.output(led_prod_ko, True)
#     else:
#         print("Código inválido. Tente novamente.")
#         avenir()

if _name_ == "_main_":
    # Comente/descomente a linha abaixo caso queira iniciar com o ativador desligado
    # GPIO.output(lib_ativador, False)  

    GPIO.output(lib_ativador, True)  # Liga o ativador
    print("Ativador acionado")

    time.sleep(5)  # Mantém ativado por 5 segundos (ajuste se necessário)

    GPIO.output(lib_ativador, False)  # Desliga o ativador
    print("Ativador desativado")

    GPIO.cleanup()  # Libera os pinos GPIO após a execução