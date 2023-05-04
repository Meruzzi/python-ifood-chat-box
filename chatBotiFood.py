# Boas vindas
print('Olá você esta no chat do ifood')

# Menu pricipal
opcao = 0
def menuNome():
    nome = input('Digite seu nome: ')
    checarNome(nome)
    print('Menu pricipal:')
    print(f'\n{nome}, digite o numero de uma opção desejada:\n')
    opcoesUsuario()

def opcoesUsuario():
    opcao = float(input("\n1 - Pedidos.\n2 - Estabelecimento.\n3 - Área de risco. \n4 - Problemas com a máquina Gertec. \n5 - Sair do atendimento.\n\nOpção: "))
    while opcao:
      if opcao != 1 and opcao !=2 and opcao != 3 and opcao != 4 and opcao != 5:
          print('Escolha uma opção entre 1 e 5: ') 
          opcoesUsuario()
          break
      if opcao == 1:
        escolhaUm()
        break
      if opcao == 2:
        escolhaDois()
        break
      if opcao == 3:
        escolhaTres()
        break
      if opcao == 4:
        escolhaQuatro()
        break
      if opcao == 5:
        print('\nO Ifood agradece o contato, boas entregas\n')
        break

# Verificar se o nome tem entre 4 e 12 caracteres. 
def checarNome(nome):
   if len(nome) <= 4 or len(nome) >= 12:
      print("Digite um nome entre 3 e 14 caracteres.")
      menuNome() 

# Primeira escolha do menu
def escolhaUm():
        print('\nPedidos: ')
        opcao = float(input("\n1 - Pedido já foi coletado.\n2 - Cliente alega que o pedido não foi entregue.\n3 - Pedido cancelado na tela.\n4 - Retorna ao menu principal \n\nOpção: "))
        while opcao:
          if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
            opcao = float(input('\nEscolha uma opção entre 1 e 4:'))
            break

          if opcao == 1:
            print("Pedido foi coletado. Qual o nome do funcionário que passou essa informação?")
            nomeFuncionario = input("Informe o nome do funcionário:")
            respostaUsuario = input("O estabelecimento vai refazer o pedido? (sim ou nao): ")
            while respostaUsuario:
              if respostaUsuario != 'sim' and respostaUsuario != 'nao':
                respostaUsuario = input("Comando invalido, digite 'sim' ou 'nao': ")             
              if respostaUsuario == 'sim':
                respostaUsuario = input("Você vai aguarda o pedido? (sim ou nao): ")
                while respostaUsuario:
                  if respostaUsuario != 'sim' and respostaUsuario != 'nao':
                    respostaUsuario = input("Comando invalido, digite 'sim' ou 'nao': ")                  
                  if respostaUsuario == 'sim':
                    print("Ficamos contentes com essa resposta. O IFOOD agradece o contato. Boas entregas e vamos pra cima.")
                    voltarMenuPrincipal()
                  if respostaUsuario == 'nao':
                    print('Estamos registrando sua taxa de relocação. Estará disponível em até 2 dias úteis.')
                    voltarMenuPrincipal()
                    break
                  break   
                break
              if respostaUsuario == 'nao':
                print('Estamos registrando sua taxa de relocação. Estará disponível em até 2 dias úteis.')
                voltarMenuPrincipal()
                break
            break        
          if opcao == 2:
              print("Por favor nos mande um print da rota finalizada:")
              print("Print enviado.")
              respostaUsuario = input("Verificaremos as informações, e em até 2 dias úteis retornaremos com a resposta. Você sofreu algum tipo de agressão? (sim ou nao): ")
              while respostaUsuario:
                if respostaUsuario != 'sim' and respostaUsuario != 'nao':
                  respostaUsuario = input("Comando invalido, digite 'sim' ou 'nao': ")  
                if respostaUsuario == 'sim':
                  print('Deixamos claro que o IFOOD repudia qualquer tipo de agressão contra seus entregadores. Vamos analisar o caso e entraremos em contato novamente para tomar as medidas cabíveis. O IFOOD agradece as informações e até o próximo contato.')
                  voltarMenuPrincipal()
                  break
                if respostaUsuario == 'nao':
                  print("Ficamos contentes que não houve nenhum tipo de agressão, nosso time está aqui para dar todo suporte . O IFOOD agradece o contato e até a próxima.")
                  voltarMenuPrincipal()
                  break
              break    
          if opcao == 3:
              periodoOcorrido = input("Por favor digite o período ocorrido (Manha, tarde ou noite): ")
              while periodoOcorrido:
                if periodoOcorrido != 'manha' and periodoOcorrido != 'tarde' and periodoOcorrido != 'noite':
                  respostaUsuario = input("Comando invalido, digite 'manha', 'tarde' ou 'noite': ")

                if respostaUsuario == 'manha' and respostaUsuario == 'tarde' and respostaUsuario == 'noite':
                  print("Verificaremos as informações, e em até 2 dias úteis retornaremos com a resposta. O IFOOD agradece o contato até a próxima.")
                  voltarMenuPrincipal()
                  break
              break      
          if opcao == 4:
              opcoesUsuario()
              break  
          
# Escolha dois do menu principal Estabelecimento
def escolhaDois():
        print('\n2 - Estabelecinemto:')
        opcao = float(input("\n1 - Estabelecimento fechado,nao consigo escanear o qrcode no estabelecimento .\n2 - Estabecimento fechado .\n3 - Pedido cancelado na tela .\n4 - Retorna ao menu principal \n\nOpção: "))
        if opcao==1:
             Atendimento_Ifood = input("Tire uma foto: ")
             print("\nEstamos realocando sua corrida, a taxa de relocação.Estará disponível em até 2 dias úteis.")
             voltarMenuPrincipal()

        if opcao==2:
             Atendimento_Ifood = input("Tire uma foto: ")
             print("\nEstamos realocando sua corrida, a taxa de relocação.Estará disponível em até 2 dias úteis.")
             voltarMenuPrincipal()


        if opcao==3:    
             entregador_Ifood = input("Insira o nome do funcionario:")        
             print("\nEstamos realocando sua corrida, a taxa de relocação estara disponível em até 2 dias úteis.")    
             voltarMenuPrincipal()

        if opcao == 4:
          opcoesUsuario() 

# Escolha do menu quatro
def escolhaTres():
      opcao = int(input("\n1 - Suspeita de roubo.\n2 - Local com Riscos Ambientais.\n3 - Voltar ao Menu Principal.\n\nOpção:  "))
    
      if opcao == 1:
          opcao = input('\nNos descreva a situação: ')
          opcao = input('\nHouve algum tipo de agressão?  ')
          while opcao:
            if opcao != 'sim' and opcao != 'nao':
                opcao = input("\nComando inválido, houve algum tipo de agressão digite 'sim' ou 'nao': ")
            if (opcao == 'sim'):
                opcao = print('\nEstamos aqui pra te dar todo o suporte. Nosso time vai entrar em contato com você em breve. O IFOOD agradece o contato e até o proximno contato. ')
                voltarMenuPrincipal()
                break
            if(opcao == 'não'):
                opcao = print('\nEstamos finalizando a corrida. Ficamos felizes que não houve nenhum tipo de agressão,nosso time está pra te dar todo suporte . O IFOOD agradece o contato e ate a proxima! ')
                voltarMenuPrincipal()
                break

      if opcao == 2:
            opcao = input('\nNos descreva a situção do local: ')
            opcao = print('\nTire uma foto do local: ')
            print('\nEstamos finalizando sua corrida. Nosso time esta aqui para de dar  todo o suporte. O IFOOD agradece e até a proxima! ')
            voltarMenuPrincipal()

      if opcao == 3:
          opcao_2 = input('\nVoltar ao menu Principal? ')
          while opcao_2:
              if opcao_2 != 'sim' and opcao_2 != 'nao':
               opcao_2 = input("\nComando inválido, Voltar ao menu Principal 'sim' ou 'nao':  ")
              if opcao_2 == 'sim' :
                opcoesUsuario()
                break
              if opcao_2 == 'não':
                print('\nO IFOOD agradece o contato. Até a Próxima!')
                break

# opcao do menu principal escolhaquatro,  4 - Problema com a máquina Gertec: submenu  opcao == 1 e opcao == 2             
def escolhaQuatro():
        print('\nProblema com a máquina Gertec: ')
        opcao = float(input('\n1 - Máquina não lê o cartão : .\n2 - Maquina não liga .\n3 - Máquina está com erro na tela: .\n4 - Voltar ao menu principal. \n\nOpção: '))
        if opcao == 1:
            print('\nMáquina não lê o cartão?\n')
            problema_maquina = input("1 - Desligue ela por 30 segundos, e depois ligue de volta e aperte a função #9, funcionou? digite 'sim' ou 'nao': ")
            
            # foi colocado o while caso a resposta for diferente de sim ou nao ele pede pra digitar sim ou nao
            while problema_maquina:
                if problema_maquina != 'sim' and problema_maquina != 'nao':
                   problema_maquina = input("\nComando invalido a maquina funcionou? digite 'sim' ou 'nao':")                                            
                if problema_maquina == 'sim':
                    problema_maquina = print("\nO IFOOD agradece o contato e até a próxima\n") 
                    voltarMenuPrincipal()
                    break
                if problema_maquina == 'nao':
                    print("\nAguarde um momento, estamos transferindo para o suporte técnico. ")
                    print('\nObrigado, o IFOOD agradece, Boas entregas')
                    voltarMenuPrincipal()
                    break
                
        if opcao == 2:
            print("\nMaquina não liga?\n")
            print('\nVerificou a bateria, faça isso, depois volte aqui no canal. ')
                                
            problema_maquina_2 = input("\nFuncionou? digite 'sim' ou 'nao': ")
            # foi colocado o while caso a resposta for diferente de sim ou nao ele pede pra digitar sim ou nao                    
            while problema_maquina_2:
                if problema_maquina_2 != 'sim' and problema_maquina_2 != 'nao':
                    problema_maquina_2 = input("\nComando invalido a maquina funcionou? digite 'sim' ou 'nao' :")

                if problema_maquina_2 == 'sim':
                    print('\nO IFOOD agradece , Boas entregas.. ')
                    voltarMenuPrincipal()
                    break      
                                    
                if problema_maquina_2 == 'nao':
                    print('\nDevolva o pedido no estabelecimento e informe o nome do funcionario')
                    input('\nNome do funcionario: ')
                    print('\nO IFOOD agradece, Voce recebera o valor da corrida em ate 5 dias uteis, Boas entregas. ')
                    voltarMenuPrincipal()
                    break
                
        if opcao == 4:
            opcoesUsuario()

#Chamar menu das opcoes principais

def voltarMenuPrincipal():
  desejaSair = input("Deseja ajuda com outro assunto? (sim ou nao): ")
  while desejaSair:
    if desejaSair != 'sim' and desejaSair != 'nao':
      desejaSair = input('Comando invalido. Digite sim ou nao: ')
    if(desejaSair == 'nao'):
      print("iFood agradece o contato.")
      break
    elif(desejaSair == 'sim'):
      opcoesUsuario()
      break


menuNome()
