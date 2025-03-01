from datetime import datetime

# Modelos disponíveis  setup 0            setup 1                setup 2
modelos = {"FXT521": "STR07000267", "FXT598": "STR07000267", "FXT551": "STR07000267"}

# Função para selecionar o setup
def selecionar_modelo():
    while True:
        modelo = input("Digite o modelo (FXT521, FXT598, FXT551): ").strip()
        if modelo in modelos:
            print(f"Modelo {modelo} selecionado. Setup: {modelos[modelo]}\n")
            return modelos[modelo]
        else:
            print("Modelo inválido. Tente novamente.\n")

# Função para validar o QR Code e data
def validar_produto(entrada_qrcode, setup, tipo, produtos_vencidos):
    try:
        cod_produto = entrada_qrcode[3:14]
        ano = entrada_qrcode[43:47]
        mes = entrada_qrcode[48:50]
        dia = entrada_qrcode[51:53]
        hora = entrada_qrcode[54:56]
        minuto = entrada_qrcode[57:59]
    except IndexError:
        print(f"{tipo} inválido! QR Code incompleto.")
        return False

    data_e_hora = datetime.now()
    ano_atual = str(data_e_hora.year)
    mes_atual = str(data_e_hora.month).zfill(2)
    dia_atual = str(data_e_hora.day).zfill(2)
    hora_atual = str(data_e_hora.hour).zfill(2)
    minuto_atual = str(data_e_hora.minute).zfill(2)

    if cod_produto == setup:
        if (ano > ano_atual or
            (ano == ano_atual and mes > mes_atual) or
            (ano == ano_atual and mes == mes_atual and dia > dia_atual) or
            (ano == ano_atual and mes == mes_atual and dia == dia_atual and hora > hora_atual) or
            (ano == ano_atual and mes == mes_atual and dia == dia_atual and hora == hora_atual and minuto >= minuto_atual)):
            print(f"{tipo} Produto dentro da validade.")
            return True
        else:
            vencimento = f"{dia}/{mes}/{ano} {hora}:{minuto}"
            print(f"{tipo} vencido - {vencimento}")
            produtos_vencidos.append((tipo, vencimento))
            return False
    else:
        print(f"QR Code inválido para {tipo}!")
        return False

# Função principal p/ alterna entre ativador e primer
def rodar_validacao():
    print("Selecione o modelo para o ATIVADOR:")
    setup_ativador = selecionar_modelo()

    print("Selecione o modelo para o PRIME:")
    setup_prime = selecionar_modelo()

    produtos_vencidos = []

    while True:
        print("\n--- Validação do ATIVADOR ---")
        ativador_ok = False
        while not ativador_ok:
            entrada_qrcode_ativador = input("Digite o QR Code do ATIVADOR: ").strip()
            ativador_ok = validar_produto(entrada_qrcode_ativador, setup_ativador, "Ativador", produtos_vencidos)
            if not ativador_ok:
                print("Reiniciando validação...\n")

        print("\nATIVADOR OK. Habilitando validação do PRIME...\n")
        
        print("--- Validação do PRIME ---")
        prime_ok = False
        while not prime_ok:
            entrada_qrcode_prime = input("Digite o QR Code do PRIME: ").strip()
            prime_ok = validar_produto(entrada_qrcode_prime, setup_prime, "Prime", produtos_vencidos)
            if not prime_ok:
                print("Reiniciando validação...\n")
        
        print("\nPRIME OK. Habilitando validação do ATIVADOR...\n")

        # Exibir produtos vencidos ao final do ciclo
        if produtos_vencidos:
            print("\nProdutos vencidos durante a validação:")
            for tipo, vencimento in produtos_vencidos:
                print(f"- {tipo}: Vencido em {vencimento}")
        else:
            print("\nNenhum produto vencido durante a validação.")

# Executar o programa
if __name__ == "__main__":
    rodar_validacao()