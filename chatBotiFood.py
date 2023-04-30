# Boas vindas
print('Olá você esta no chat do ifood')

# Menu pricipal
opcao = 0
def menuPrincipal():
    nome = input('Digite seu nome: ')
    checarNome(nome)
    print('Menu pricipal:')
    print(f'\n{nome}, digite o numero de uma opção desejada:\n')
    opcao = float(input("\n1 - Pedidos.\n2 - Estabelecimento.\n3 - Área de risco .\n4 - Problemas com a máquina Gertec.\n5 - Sair do atendimento.\n\nOpção: "))
    if opcao == 1:
        escolhaUm()
    if opcao == 2:
        escolhadois()
    if opcao == 4:
        escolhaquatro()
    if opcao == 5:
        print('\nO IFOOD agradece, o contato Boas entregas\n')
    #elif opcao == 2:
        #print('Outras opções')

# Verificar se o nome tem entre 4 e 8 caracteres. 
def checarNome(nome):
   if len(nome) <= 4 or len(nome) >= 12:
      print("Digite um nome entre 4 e 8 caracteres.")
      menuPrincipal() 

# Primeira escolha do menu
def escolhaUm():
        print('\nPedidos: ')
        opcao = float(input("\n1 - Pedido já foi coletado.\n2 - Cliente alega que o pedido não foi entregue.\n3 - Pedido cancelado na tela.\n4 - Retorna ao menu principal \n\nOpção: "))
        if opcao == 1:
             print("Pedido foi coletado. Qual o nome do funcionário que passou essa informação?")
             nomeFuncionario = input("Informe o nome do funcionário:")
             respostaUsuario = input("O estabelecimento vai refazer o pedido? (sim ou nao): ")
             if respostaUsuario == 'sim':
                  respostaUsuario = input("Você vai aguarda o pedido? (sim ou nao): ")
                  if(respostaUsuario == 'sim'):
                    print("Ficamos contentes com essa resposta. O IFOOD agradece o contato. Boas entregas e vamos pra cima.")
                    desejaSair = input("Deseja ajuda com outro assunto? (sim ou nao): ")
                    if(desejaSair == 'nao'):
                      print("iFood agradece o contato.")
                    elif(desejaSair == 'sim'):
                        menuPrincipal()
                  if respostaUsuario == 'nao':
                    print('Estamos registrando sua taxa de relocação. Estará disponível em até 2 dias úteis.')
                    desejaSair = input("Deseja ajuda com outro assunto? (sim ou nao): ")
                    if(desejaSair == 'nao'):
                      print("iFood agradece o contato.")
                    elif(desejaSair == 'sim'):
                      menuPrincipal()
            
             if respostaUsuario == 'nao':
              print('Estamos registrando sua taxa de relocação. Estará disponível em até 2 dias úteis.')
              respostaUsuario = input("Deseja ajuda com outro assunto? (sim ou nao): ")
              if(respostaUsuario == 'nao'):
                  print("iFood agradece o contato.")
              elif(respostaUsuario == 'sim'):
                  menuPrincipal()

        if opcao == 2:
            print("Por favor nos mande um print da rota finalizada:")
            print("Print enviado.")
            respostaUsuario = input("Verificaremos as informações, e em até 2 dias úteis retornaremos com a resposta. Você sofreu algum tipo de agressão? (sim ou nao): ")
            if(respostaUsuario == 'sim'):
                print('Deixamos claro que o IFOOD repudia qualquer tipo de agressão contra seus entregadores. Vamos analisar o caso e entraremos em contato novamente para tomar as medidas cabíveis. O IFOOD agradece as informações e até o próximo contato.')
                desejaSair = input("Deseja ajuda com outro assunto? (sim ou nao): ")
                if(desejaSair == 'nao'):
                    print("iFood agradece o contato.")
                elif(desejaSair == 'sim'):
                    menuPrincipal()
            if(respostaUsuario == 'nao'):
                print("Ficamos contentes que não houve nenhum tipo de agressão, nosso time está aqui para dar todo suporte . O IFOOD agradece o contato e até a próxima.")
                desejaSair = input("Deseja ajuda com outro assunto? (sim ou nao): ")
                if(desejaSair == 'nao'):
                    print("iFood agradece o contato.")
                elif(desejaSair == 'sim'):
                    menuPrincipal()

        if opcao == 3:
            periodoOcorrido = input("Por favor digite o período ocorrido (Manha, tarde ou noite): ")
            print("Verificaremos as informações, e em até 2 dias úteis retornaremos com a resposta. O IFOOD agradece o contato até a próxima.")
            desejaSair = input("Deseja ajuda com outro assunto? (sim ou nao): ")
            if(desejaSair == 'nao'):
              print("iFood agradece o contato.")
            elif(desejaSair == 'sim'):
              menuPrincipal()

        if opcao == 4:
             desejaSair = input("Deseja voltar ao menu principal? (sim ou nao): ")
             if(desejaSair == 'nao'):
                print("iFood agradece o contato. Até a próxima!")
             elif(desejaSair == 'sim'):
                menuPrincipal()
                
# Escolha dois do menu principal Estabelecimento
def escolhadois():
        print('\n2 - Estabelecinemto:')
        opcao = float(input("\n1 - Estabelecimento fechado,nao consigo escanear o qrcode no estabelecimento .\n2 - Estabecimento fechado .\n3 - Pedido cancelado na tela .\n4 - Retorna ao menu principal \n\nOpção: "))
        if opcao==1:

             Atendimento_Ifood=input("Tira uma foto")
             print("\nEstamos realocando sua corrida, a taxa de relocação.Estará disponível em até 2 dias úteis.")


             print("\nO IFOOD agradece o contato. Até a próxima!")



        if opcao==2:

             Atendimento_Ifood=input("Tira uma foto")
             print("\nEstamos realocando sua corrida, a taxa de relocação.Estará disponível em até 2 dias úteis.")


             print("\nO IFOOD agradece o contato. Até a próxima!")


        if opcao==3:
             
             entregador_Ifood=input("Nome do Funcionario")        
             print("\nEstamos realocandosua corrida, ataxa de relocação.Estará disponívelem até 2 dias úteis.")
             
             print("\nO IFOOD agradece o contato. Até a próxima!")

        if opcao == 4:
             menuPrincipal()  


                

# opcao do menu principal 4 4 - Problema com a máquina Gertec: sub menu 1 e 2             
def escolhaquatro():
        print('\nProblema com a máquina Gertec: ')
        opcao = float(input('\n1 - Máquina não lê o cartão : .\n2 - Maquina não liga .\n3 - Máquina está com erro na tela: .\n4 - Voltar ao menu principal. \n\nOpção: '))
        if opcao == 1:
            print('\nMáquina não lê o cartão?\n')
            problema_maquina = input("1 - Desligue ela por 30 segundos, e depois ligue de volta e aperte a função #9, funcionou? digite 'sim ou nao': ")
            
            # foi colocado o while caso a resposta for diferente de sim ou nao ele pede pra digitar sim ou nao
            problema_maquina == 'sim' or 'nao'
            while   (problema_maquina  != 'sim') or (problema_maquina  != 'nao'):
                problema_maquina = input("\nComando invalido a maquina funcionou? digite 'sim ou nao':")
                           
                if problema_maquina == 'sim':
                    problema_maquina = print("\nO IFOOD agradece o contato e até a próxima\n") 
                    break
                if problema_maquina == 'nao':
                    print("\nAguarde um momento, estamos transferindo para o suporte técnico. ")
                    print('\nObrigado, o IFOOD agradece, Boas entregas')
                    break

        if opcao == 2:
                print("\nMaquina não liga?\n")
                problema_maquina_2 = input("Verificou a bateria digite 'sim ou nao'? ")
                print('\nFaça isso, depois volte aqui no canal. ')
                problema_maquina_2 == input("\nfunciono? digite 'sim' ou 'nao': ")
                if problema_maquina_2 == 'sim':
                    print('\nO IFOOD agradece , Boas entregas.. ')
                              
                if problema_maquina_2 == 'nao':
                    print('\nDevolva o pedido no estabelecimento e informe o nome do funcionario')
                    input('\nNome do funcionario: ')
                    print('\nO IFOOD agradece, Voce recebera o valor da corrida em ate 5 dias uteis, Boas entregas. ')


        
             

        if opcao == 4:
             menuPrincipal()


# Chamar função principal
menuPrincipal()

