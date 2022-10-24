listacadastrodeprodutos = []
#-------------------------- FUNÇÕES ----------------------------
#----------------------- cadastrarProduto ----------------------
def cadastrarProduto(codigo): #Cadastra os produtos conforme os dados solicitados, após isso é jogado em um dicionário e em seguida em uma lista.
    print('Você selecionou a opção de cadastrar produto')
    print('O código do produto é {}' .format(codigo))
    nome = input('Informe o NOME do produto: ')
    fabricante = input('Informe o FABRICANTE do produto: ')
    valor = float(input('Informe o Valor do produto: R$ '))
    dicionario_cadastro = {'CÓDIGO': codigo, #Armazena os dados dos produtos
                           'NOME': nome,
                           'FABRICANTE': fabricante,
                           'VALOR': valor}
    listacadastrodeprodutos.append(dicionario_cadastro.copy())

#---------------------- consultarProduto -----------------------
def consultarProduto():
    while True:
        print('Você selecionou a opção de Consultar Produto')  #É ativada quando o usuário digita o número 2 no menu principal
        try:
            opConsultar = int(input('Escolha a Opção Desejada:\n'
                                    '1 - Consultar Todos os Produtos\n'
                                    '2 - Consultar Produtos por Código\n'
                                    '3 - Consultar Produtos por Fabricante\n'
                                    '4 - Retornar ao Menu Anterior\n'
                                    '>> '))
            if opConsultar == 1:
                print('Bem-vindo ao menu consultar TODOS os Produtos.')
                for produtos in listacadastrodeprodutos: #Consulta os prudutos dentro da lista (listacadastrodeprodutos)
                    for key, value in produtos.items(): #Chama os itens dentro do dicionário cadastros.
                        print('{} : {} ' .format(key, value))

            elif opConsultar == 2:
                print('Bem-vindo ao menu Consultar por CÓDIGO')
                entrada = int(input('Digite o Código desejado:\n >> '))
                for produtos in listacadastrodeprodutos:
                    if produtos['CÓDIGO'] == entrada: #Pesquida o Código do produto dentro do dicionário.
                        for key, value in produtos.items():
                            print('{} : {} '.format(key, value))

            elif opConsultar == 3:
                print('Bem-vindo ao menu Consultar por FABRICANTE')
                entrada = input('Digite o Fabricante desejado:\n >> ')
                for produtos in listacadastrodeprodutos:
                    if produtos['FABRICANTE'] == entrada: #Pesquisa o fabricante de acordo com o nome.
                        for key, value in produtos.items():
                            print('{} : {} '.format(key, value))

            elif opConsultar == 4:
                print('Retornando ao menu anterior...')
                break

            else:
                print('Digite uma opção válida!')

        except ValueError:
            print('Pare de digitar valores não numéricos!')

#---------------------- removerProduto  ------------------------
def removerProduto():
    print('Você selecionou a opção de remover produto')
    entrada = int(input('Digite o CÓDIGO desejado:\n >> '))
    for produtos in listacadastrodeprodutos:
        if produtos['CÓDIGO'] == entrada:
            listacadastrodeprodutos.remove(produtos) #Remove o produto de dentro da listacadastrodeprodutos
            print('Produto com o código {} foi removido' .format(entrada))
        else:
            print('Pare de digitar valores não numéricos')

#------------------------- INÍCIO MAIN -------------------------
print('Bem-vindo ao Controle de Estoque da Mercearia Ivan Reis Fernandes')
cadastro_de_produto = 0
while True:
    try:
        opcao = int(input('Escolha a opção desejada: \n'
              '1 - Cadastrar Produto\n'
              '2 - Consultar Produto(s) \n'
              '3 - Remover Produto\n'
              '4 - Sair\n'
              '>> '))
        if opcao == 1: #Está sessão chama as funções, de acordo com a escolha do usuário.
            cadastro_de_produto += 1
            cadastrarProduto(cadastro_de_produto)
        elif opcao == 2:
            consultarProduto()
        elif opcao == 3:
            removerProduto()
        elif opcao == 4:
            break #Finaliza o programa caso o usuário digite 4.
        else:
            print('Por favor digite a uma opção válida')

    except ValueError:
        print('Pare de digitar valores não numéricos!')



