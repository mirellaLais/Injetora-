from datetime import datetime
#           setup 1        setup 2       setup 3
setups = ["STR07000267","STR07000267","STR07000267"] #PRIMER
habilita = True


#modelo escolhido para rodar
while habilita:
    if habilita:
        avenir_ = input("digite o codigo avenrir: ")
        if avenir_ == "FXT521":
            indice = 1
            habilita = False
        elif avenir_ == "FXT598":
            indice = 2
            habilita = False
        elif avenir_ == "FXT551":
            indice = 3
            habilita = False
        elif avenir_ == "------":
            indice = 4
            habilita = False
        elif avenir_ == "------":
            indice = 5
            habilita = False
        else:
            indice = 0
        print("indice é = ", indice)

       
while indice == 1:
    data_e_hora = datetime.now()
    data_e_hora.strftime('%d/%m/%Y %H:%M')
    
    entrada_qrcode  = input("Digte o QR Code: ")
    cod_produto     = entrada_qrcode[3:14]
    ano             = entrada_qrcode[43:47]
    mes             = entrada_qrcode[48:50]
    dia             = entrada_qrcode[51:53]
    hora            = entrada_qrcode[54:56]
    minuto          = entrada_qrcode[57:59]
    
    ano_atual             = str(data_e_hora.year)
    mes_atual             = str(data_e_hora.month)
    dia_atual             = str(data_e_hora.day)
    hora_atual            = str(data_e_hora.hour)
    minuto_atual          = str(data_e_hora.minute)
    habilita = True
    

    if cod_produto == setups[0]:
        if ano > ano_atual:
           produto = True
           
        elif ano == ano_atual:
            if mes > mes_atual:
                produto = True

            elif mes == mes_atual:
                if dia > dia_atual:
                    produto = True

                elif dia == dia_atual:
                    if hora > hora_atual:
                        produto = True
                        
                    elif hora == hora_atual:
                        if minuto >= minuto_atual:
                            produto = True
                        else:
                            produto = False
                            print("produto vencido minuto") 
                    else:
                        produto = False
                        print("produto vencido hora") 
                else:
                    produto = False
                    print("produto vencido dia")         
            else:
                produto = False
                print("produto vencido mes") 
        else:
            produto = False
            print("produto vencido ano") 


    else:
        print("qr code invalido")        
    break


while indice == 2:
    data_e_hora = datetime.now()
    data_e_hora.strftime('%d/%m/%Y %H:%M')
    
    entrada_qrcode  = input("Digte o QR Code: ")
    cod_produto     = entrada_qrcode[3:14]
    ano             = entrada_qrcode[43:47]
    mes             = entrada_qrcode[48:50]
    dia             = entrada_qrcode[51:53]
    hora            = entrada_qrcode[54:56]
    minuto          = entrada_qrcode[57:59]
    
    ano_atual             = str(data_e_hora.year)
    mes_atual             = str(data_e_hora.month)
    dia_atual             = str(data_e_hora.day)
    hora_atual            = str(data_e_hora.hour)
    minuto_atual          = str(data_e_hora.minute)
    habilita = True
    
    #verificação de validade primer
    if cod_produto == setups[1]:
        if ano > ano_atual:
           produto = True
        elif ano == ano_atual:
            if mes > mes_atual:
                produto = True

            elif mes == mes_atual:
                if dia > dia_atual:
                    produto = True

                elif dia == dia_atual:
                    if hora > hora_atual:
                        produto = True
                        
                    elif hora == hora_atual:
                        if minuto >= minuto_atual:
                            produto = True
                        else:
                            produto = False
                            print("produto vencido minuto") 
                    else:
                        produto = False
                        print("produto vencido hora") 
                else:
                    produto = False
                    print("produto vencido dia")         
            else:
                produto = False
                print("produto vencido mes") 
        else:
            produto = False
            print("produto vencido ano") 


    else:
        print("qr code invalido")        
    
while indice == 3:
    data_e_hora = datetime.now()
    data_e_hora.strftime('%d/%m/%Y %H:%M')
    
    entrada_qrcode  = input("Digte o QR Code: ")
    cod_produto     = entrada_qrcode[3:14]
    ano             = entrada_qrcode[43:47]
    mes             = entrada_qrcode[48:50]
    dia             = entrada_qrcode[51:53]
    hora            = entrada_qrcode[54:56]
    minuto          = entrada_qrcode[57:59]
    
    ano_atual             = str(data_e_hora.year)
    mes_atual             = str(data_e_hora.month)
    dia_atual             = str(data_e_hora.day)
    hora_atual            = str(data_e_hora.hour)
    minuto_atual          = str(data_e_hora.minute)
    habilita = True
    
    
    if cod_produto == setups[2]:
        if ano > ano_atual:
           produto = True
        elif ano == ano_atual:
            if mes > mes_atual:
                produto = True

            elif mes == mes_atual:
                if dia > dia_atual:
                    produto = True

                elif dia == dia_atual:
                    if hora > hora_atual:
                        produto = True
                        
                    elif hora == hora_atual:
                        if minuto >= minuto_atual:
                            produto = True
                        else:
                            produto = False
                            print("produto vencido minuto") 
                    else:
                        produto = False
                        print("produto vencido hora") 
                else:
                    produto = False
                    print("produto vencido dia")         
            else:
                produto = False
                print("produto vencido mes") 
        else:
            produto = False
            print("produto vencido ano") 


    else:
        print("qr code invalido")        
    

