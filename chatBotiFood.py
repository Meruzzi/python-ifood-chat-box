# Boas vindas
print('Olá você esta no chat do ifood')

# Verificar se o nome tem entre 4 e 8 caracteres.
def checarNome(nome):
   if len(nome) <= 4 or len(nome) >= 8:
      print("Digite um nome entre 4 e 8 caracteres.")
      menuPrincipal()

# Menu pricipal
opcao = 0
def menuPrincipal():
    nome = input('Digite seu nome: ')
    checarNome(nome)
    print('Menu pricipal:')
    print(f'\n{nome}, Digite o numero de uma opção desejada:\n')
    opcao = float(input("\n1 - Pedidos.\n2 - Estabelecimento.\n3 - Área de risco .\n4 - Problemas com a máquina Gertec.\n5 - Sair do atendimento.\n\nOpção: "))
    if opcao == 1:
        escolhaUm()
    elif opcao == 2:
        print('Outras opções')

# Primeira escolha do menu
def escolhaUm():
        print('\nPedidos: ')
        opcao = float(input("\n1 - Pedido já foi coletado .\n2 - Cliente alega que o pedido não foi entregue .\n3 - Pedido cancelado na tela .\n4 - Retorna ao menu principal \n\nOpção: "))
        if opcao == 1:
             print("Pedido foi coletado. Qual o nome do funcionário que passou essa informação?")
             nomeFuncionario = input("Informe o nome do funcionário:")
             respostaUsuario = input("O estabelecimento vai refazer o pedido? (sim ou nao)")
             if respostaUsuario == 'sim':
                  respostaUsuario = input("Você vai aguarda o pedido? (sim ou nao)")
                  if respostaUsuario == 'sim':
                    print("Ficamos contentes com essa resposta. O IFOOD agradece o contato. Boas entregas e vamos pra cima.")
                    respostaUsuario = input("Deseja ajuda com outro assunto? (sim ou nao)")
                  if(respostaUsuario == 'nao'):
                    print("iFood agradece o contato.")
                  if(respostaUsuario == 'sim'):
                    menuPrincipal()
                  if respostaUsuario == 'nao':
                    print('Estamos registrando sua taxa de relocação. Estará disponível em até 2 dias úteis.')
                  respostaUsuario = input("Deseja ajuda com outro assunto? (sim ou nao)")
                  if(respostaUsuario == 'nao'):
                    print("iFood agradece o contato.")
                  if(respostaUsuario == 'sim'):
                    menuPrincipal()
            
             if respostaUsuario == 'nao':
              print('Estamos registrando sua taxa de relocação. Estará disponível em até 2 dias úteis.')
              respostaUsuario = input("Deseja ajuda com outro assunto? (sim ou nao)")
              if(respostaUsuario == 'nao'):
                  print("iFood agradece o contato.")
              if(respostaUsuario == 'sim'):
                  menuPrincipal()

        if opcao == 2:
            print("Por favor nos mande um print da rota finalizada:")
            print("Print enviado.")
            respostaUsuario = input("Verificaremos as informações, e em até 2 dias úteis retornaremos com a resposta. Você sofreu algum tipo de agressão? (sim ou nao)")
            if(respostaUsuario == 'sim'):
                print('Deixamos claro que o IFOOD repudia qualquer tipo de agressão contra seus entregadores. Vamos analisar o caso e entraremos em contato novamente para tomar as medidas cabíveis. O IFOOD agradece as informações e até o próximo contato.')
                respostaUsuario = input("Deseja ajuda com outro assunto? (sim ou nao)")
                if(respostaUsuario == 'nao'):
                    print("iFood agradece o contato.")
                if(respostaUsuario == 'sim'):
                    menuPrincipal()
            if(respostaUsuario == 'nao'):
                print("Ficamos contentes que não houve nenhum tipo de agressão, nosso time está aqui para dar todo suporte . O IFOOD agradece o contato e até a próxima.")
                respostaUsuario = input("Deseja ajuda com outro assunto? (sim ou nao)")
                if(respostaUsuario == 'nao'):
                    print("iFood agradece o contato.")
                if(respostaUsuario == 'sim'):
                    menuPrincipal()

        if opcao == 3:
            periodoOcorrido = input("Por favor digite o período ocorrido: (Manha, tarde ou noite)")
            print("Verificaremos as informações, e em até 2 dias úteis retornaremos com a resposta. O IFOOD agradece o contato até a próxima.")
            respostaUsuario = input("Deseja ajuda com outro assunto? (sim ou nao)")
            if(respostaUsuario == 'nao'):
              print("iFood agradece o contato.")
            if(respostaUsuario == 'sim'):
              menuPrincipal()

        if opcao == 4:
             respostaUsuario = input("Deseja voltar ao menu principal? (sim ou nao)")
             if(respostaUsuario == 'nao'):
                print("iFood agradece o contato. Até a próxima!")
             if(respostaUsuario == 'sim'):
                menuPrincipal()


# Chamar função principal
menuPrincipal()

