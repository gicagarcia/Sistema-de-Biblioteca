'''
Trabalho da disciplina Algoritmos de Programação 1
Alunos: Giovana Rocha Garcia e Guilherme Orlandi
Tema: Biblioteca
'''
import json
encoding = 'utf-8'
#Função para chamar o menu principal
def menu (matriz_usuarios, matriz_livrocad, dicionarios_emprestimo):
    menu = int(input("Menu de opções: \n 1. Submenu de Usuários \n 2. Submenu de Livros \n 3. Submenu de emprestimos \n 4. Submenu de relatórios \n -1. Sair \n Opção: "))
    if menu == 1:
        print(submenu_user(matriz_usuarios, matriz_livrocad, dicionarios_emprestimo))
    elif menu == 2:
        print(submenu_livro(matriz_usuarios, matriz_livrocad, dicionarios_emprestimo))
    elif menu == 3:
        print(submenu_emprestimo(matriz_usuarios, matriz_livrocad, dicionarios_emprestimo))
    elif menu == 4:
        print(submenu_relatorios(matriz_usuarios, matriz_livrocad, dicionarios_emprestimo))
    elif menu == -1:
        print("Programa encerrado. Obrigada!")
    else:
        print("Opção inválida. Tente novamente.")
        menu()

#Função do submenu usuários
def submenu_user(matriz_usuarios, matriz_livrocad, dicionarios_emprestimo):
    print('=========Submenu de usuários=========')
    opcao = 1
    while opcao > 0:
        matriz_usuarios = matriz_user() #### Atualizando a matriz para constar novos cadastros nas demais funções ######
        opcao = int(input("O que deseja fazer? \n 1. Listar todos os usuários \n 2. Listar um usuário específico \n 3. Incluir um usuário \n 4. Alterar usuário \n 5. Excluir usuário \n -1. Voltar \n Opção: "))
        if opcao == 1: #listar todos
            listar_usuarios(matriz_usuarios, matriz_livrocad)
        elif opcao == 2: #listar elemento específico
            lista_especifico_user(matriz_usuarios, matriz_livrocad)
        elif opcao == 3: #incluir
            cadastro_usuario(matriz_usuarios, matriz_livrocad)
        elif opcao == 4: #alterar
            alterar_user(matriz_usuarios, matriz_livrocad) 
        elif opcao == 5: #excluir
            excluir_user(matriz_usuarios, matriz_livrocad)
        elif opcao == -1: #voltar
            menu(matriz_usuarios, matriz_livrocad, dicionarios_emprestimo)

#Função do submenu livros
def submenu_livro(matriz_usuarios, matriz_livrocad, dicionarios_emprestimo):
    print('=========Submenu de livros=========')
    opcao = 1
    while opcao > 0:
        matriz_livrocad = matriz_livros() ###### Atualizando a matriz para constar novos cadastros nas demais funções #######
        opcao = int(input("O que deseja fazer? \n 1. Listar todos os livros \n 2. Listar um livro específico \n 3. Incluir um livro \n 4. Alterar um livro \n 5. Excluir livro \n -1. Voltar \n Opção: "))
        if opcao == 1: #listar todos
            listar_livros(matriz_usuarios, matriz_livrocad)
        elif opcao == 2: #listar elemento específico
            lista_especifico_livro(matriz_usuarios, matriz_livrocad) 
        elif opcao == 3: #incluir
            cadastro_livros(matriz_usuarios, matriz_livrocad)
        elif opcao == 4: #alterar
            alterar_livro(matriz_livrocad,matriz_usuarios)
        elif opcao == 5: #excluir
            excluir_livro(matriz_livrocad, matriz_usuarios)
        elif opcao == -1: #voltar
            menu(matriz_usuarios,matriz_livrocad,dicionarios_emprestimo)

#Função do submenu usuários
def submenu_emprestimo(matriz_usuarios, matriz_livrocad, dicionarios_emprestimo):
    print('=========Submenu de emprestimo=========')
    opcao = 1
    while opcao > 0:
        dicionarios_emprestimo = dicionarios()
        opcao = int(input("O que deseja fazer? \n 1. Listar todos os emprestimos \n 2. Listar um emprestimo específico \n 3. Incluir emprestimo \n 4. Alterar emprestimo \n 5. Excluir emprestimo \n -1. Voltar \n Opção: "))
        if opcao == 1: #listar todos
            listar_emprestimos(matriz_usuarios, matriz_livrocad, dicionarios_emprestimo)
        elif opcao == 2: #listar elemento específico
            lista_especifico_emprestimo(matriz_usuarios, matriz_livrocad, dicionarios_emprestimo)
        elif opcao == 3: #incluir
            cadastro_emprestimo(matriz_usuarios, matriz_livrocad, dicionarios_emprestimo)
        elif opcao == 4: #alterar
            alterar_emprestimo(matriz_usuarios, matriz_livrocad, dicionarios_emprestimo)
        elif opcao == 5: #excluir
            excluir_emprestimo(matriz_usuarios, matriz_livrocad, dicionarios_emprestimo)
        elif opcao == -1: #voltar
            menu(matriz_usuarios, matriz_livrocad, dicionarios_emprestimo)

#Função do submenu de relatórios
def submenu_relatorios(matriz_usuarios, matriz_livrocad, dicionarios_emprestimo):
    print('=========Submenu de relatórios=========')
    opcao = 1
    while opcao > 0:
        #relatorio dict
        print('Escolha sua opcao:' )
        opcao = int(input("O que deseja fazer? \n 1. Mostrar usuários baseado em idade \n 2. Mostrar livro baseado em autores \n 3. Mostrar emprestimos baseado em devolução \n -1. Voltar \n Opção:"))
        if opcao == 1: #Baseado em idade
            relatorioA(matriz_usuarios)
        elif opcao == 2: #listar elemento específico
            relatorioB(matriz_livrocad) #baseado em autor
        elif opcao == 3: #incluir
            relatorioC(matriz_usuarios, matriz_livrocad, dicionarios_emprestimo)  ##baseado em data 
        elif opcao == -1: #voltar
            menu(matriz_usuarios, matriz_livrocad, dicionarios_emprestimo)

            
###############################################  FUNÇÕES QUE CRIAM A MATRIZ OU A LISTA DE DICIONÁRIOS A PARTIR DOS DADOS EM ARQUIVO  ###############################################
######### A ideia para essas funções foi transfarmar os arquivos texto em matrizes ou uma lista de dict, para facilitar a manipulação dos dados e manter um padrão de escritas

def matriz_user(): #criando a matriz a partir do arquivo de usuários
    leitura = open('usuarios.txt', 'r')
    dados = leitura.readlines()
    matriz = []
    for i in range(len(dados)):
        lista = json.loads(dados[i].replace("\'", "\""))
        matriz.append(lista)
    leitura.close()
    return matriz

def matriz_livros(): #criando a matriz a partir do arquivo de livros 
    leitura = open('livros.txt', 'r')
    dados = leitura.readlines()
    matriz = []
    for i in range(len(dados)):
        lista = json.loads(dados[i].replace("\'", "\""))
        matriz.append(lista)
    leitura.close()
    return matriz

def dicionarios(): #criando uma lista de dicionários a partir do arquivo de empréstimos
    leitura = open('emprestimos.txt', 'r')
    lista = []
    dic = leitura.readlines()
    for linha in dic:
        dicio = json.loads(linha.replace("\'", "\""))
        lista.append(dicio)
    leitura.close()
    return lista

##################################################################  FUNÇÕES PARA LISTAR TUDO   #######################################################################################

#Função para listar todos os usuários 
def listar_usuarios(matriz_usuarios, matriz_livrocad):
    for linha in range(len(matriz_usuarios)):
        print(f"{'*' * 25} \n CPF: {matriz_usuarios[linha][0]} \n Nome: {matriz_usuarios[linha][1]} \n Endereço: {matriz_usuarios[linha][2]}, {matriz_usuarios[linha][3]} \n CEP: {matriz_usuarios[linha][4]} \n E-mail(s): {matriz_usuarios[linha][5]} \n Telefone(s): {matriz_usuarios[linha][6]} \n Data de nascimento: {matriz_usuarios[linha][7]} \n Profissão: {matriz_usuarios[linha][8]}")
        print('\n')

#Função para listar todos os livros
def listar_livros(matriz_usuarios, matriz_livrocad):
    for linha in range(len(matriz_livrocad)):
        print(f"{'*' * 25} \n ISBN: {matriz_livrocad[linha][0]} \n Título: {matriz_livrocad[linha][1]} \n Gênero: {matriz_livrocad[linha][2]} \n Autores: {matriz_livrocad[linha][3]} \n Número de páginas: {matriz_livrocad[linha][4]}")
        print('\n')

#Função para listar todos os empréstimos
def listar_emprestimos(matriz_usuarios, matriz_livrocad, dicionarios_emprestimo):
    for linha in dicionarios_emprestimo:
        print(linha)


##################################################################  FUNÇÕES DE LISTAGEM ESPECÍFICA   #######################################################################################

#Função para listar usuário específico:
def lista_especifico_user(matriz_usuarios, matriz_livrocad):
    elemento = str(input("Informe o CPF do usuário que deseja listar: "))
    indice = percorrer(elemento, matriz_usuarios)
    if indice < 0:
            print('Usuário não consta em nosso sistema.')
    else:
        print(f"{'*' * 25} \n CPF: {matriz_usuarios[indice][0]} \n Nome: {matriz_usuarios[indice][1]} \n Endereço: {matriz_usuarios[indice][2]}, {matriz_usuarios[indice][3]} \n CEP: {matriz_usuarios[indice][4]} \n E-mail(s): {matriz_usuarios[indice][5]} \n Telefone(s): {matriz_usuarios[indice][6]} \n Data de nascimento: {matriz_usuarios[indice][7]} \n Profissão: {matriz_usuarios[indice][8]}")

#Função para listar um livro específico:
def lista_especifico_livro(matriz_usuarios, matriz_livrocad):
    elemento = str(input("Informe o ISBN do livro que deseja listar: "))
    indice = percorrer(elemento, matriz_livrocad)
    if indice < 0:
            print('Este livro não consta em nosso sistema.')
    else:
        print(f"{'*' * 25} \n ISBN: {matriz_livrocad[indice][0]} \n Título: {matriz_livrocad[indice][1]} \n Gênero: {matriz_livrocad[indice][2]},\n Autor/a {matriz_livrocad[indice][3]} \n Número de páginas: {matriz_livrocad[indice][4]}")

#Função para listar um empréstimo específico:
def lista_especifico_emprestimo(matriz_usuarios, matriz_livrocad, dicionarios_emprestimo):
    elemento1 = str(input("Informe o CPF: "))
    elemento2 = str(input("Informe o ISBN: "))
    elemento3 = str(input("Informe a data de retirada (dd/mm): "))
    for dicionario in dicionarios_emprestimo:
        if elemento1 == dicionario['CPF'] and elemento2 == dicionario['ISBN'] and elemento3 == dicionario['Data de retirada']:
            print(dicionario)
            return True
    return print("Empréstimo não encontrado.")

#################################################################    FUNÇÕES PARA CADASTRAR OS DADOS    #######################################################################################

#Função de cadastro de usuários no sistema
def cadastro_usuario(matriz_usuarios, matriz_livrocad): 
    with open('usuarios.txt', 'a') as escrita_user: 
        Linha = []
        print("Informe os dados do usuário que deseja cadastrar: ")
        CPF = str(input("CPF do usuário (apenas dígitos): ")).replace('-','').replace('.','').replace(' ','')
        existe = 0
        while existe >= 0: 
            while CPF.isdigit() == False:
                print("CPF inválido. Informe novamente com apenas dígitos: ")
                CPF = str(input("CPF do usuário: ")).replace('-','').replace('.','').replace(' ','')
            existe = percorrer(CPF, matriz_usuarios)
            if existe >= 0:
                print("Usuário já cadastrado. Informe novamente.")
                CPF = str(input("CPF do usuário (apenas dígitos): ")).replace('-','').replace('.','').replace(' ','')
        Linha.append(CPF)
        nome = str(input("Nome: "))
        Linha.append(nome)
        print("Dados do endereço: ")
        rua = str(input("Rua: "))
        Linha.append(rua)
        nro = str(input("Número: "))
        while nro.isdigit() == False:
            print("Número inválido. Informe novamente:")
            nro = str(input("Número: "))
        Linha.append(nro)
        cep = str(input("Digite o CEP (apenas dígitos, ex: 13570060): ")).replace('-','').replace('.','').replace(' ','')
        while cep.isdigit() == False:
            print('Seu CEP está inválido')
            cep = str(input("Digite o CEP (apenas dígitos, ex: 13570060): ")).replace('-','').replace('.','').replace(' ','')
        else:
            Linha.append(cep)
            emails = []
            num_emails = int(input("Quantos e-mails você deseja informar? "))
            i = 0
            while i < num_emails:
                email = str(input("Informe o e-mail: ")) #arrumar aqui para o usuário poder informar quantos quiser
                emails.append(email)
                i += 1
            Linha.append(emails)
            telefones = []
            num_telefones = int(input("Quantos telefones você deseja informar? "))
            i = 0
            while i < num_telefones:
                telefone = str(input("Telefone com DDD (apenas digitos, ex: 16996334100): ")).replace('-','').replace('.','').replace(' ','')
                while telefone.isdigit() == False:
                    print('Seu telefone está inválido')
                    telefone = str(input("Telefone com DDD (informe sem pontos, traços ou parênteses): ")).replace('-','').replace('.','').replace(' ','')
                telefones.append(telefone)
                i += 1
            Linha.append(telefones)
            nascimento = str(input("Data de nascimento: "))
            Linha.append(nascimento)
            profissao = str(input("Qual a profissão? "))
            Linha.append(profissao)
            print("Usuário cadastrado.")
        escrita_user.write(str(Linha))
        escrita_user.write('\n')


#Função de cadastro de livros no sistema
def cadastro_livros(matriz_usuarios, matriz_livrocad): #cadastro de livros no sistema
    with open('livros.txt', 'a') as escrita_livros:
        Linha = []
        print("Informe as informações do livro que deseja cadastrar: ")
        ISBN = str(input("ISBN do livro (apenas dígitos): ")).replace('-','').replace('.','').replace(' ','')
        existe = 0
        while existe >= 0:
            while ISBN.isdigit() == False:
                print("ISBN inválido. Informe somente dígitos. ")
                ISBN =str(input("ISBN apenas digitos: ")).replace('-','').replace('.','').replace(' ','')
            existe = percorrer(ISBN,matriz_livrocad)
            if existe >= 0:
                print('Seu ISBN já está cadastrado, digite novamente.')
                ISBN =str(input("ISBN apenas com digitos: ")).replace('-','').replace('.','').replace(' ','')
        while ISBN.isdigit() == False:
            print("ISBN inválido. Informe somente dígitos. ")
            ISBN =str(input("ISBN apenas digitos: ")).replace('-','').replace('.','').replace(' ','')
        Linha.append(ISBN)
        titulo = str(input("Título do livro: "))
        Linha.append(titulo)
        genero = str(input("Qual o gênero? "))
        Linha.append(genero)
        autores = []
        num_autores = str(input("Quantos autores o livro tem? Informe apenas o número: "))
        while num_autores.isdigit() == False:
            print('Quantidade de autores está inválido, digite novamente')
            num_autores = str(input("Quantos autores o livro tem? Informe apenas o número: "))
        num_autores=int(num_autores)
        i = 0
        while i < num_autores:
            nome_autor = str(input("Nome do autor: "))
            autores.append(nome_autor)
            i+=1
        Linha.append(autores)
        paginas = str(input("Qual o número de páginas do livro? "))
        while paginas.isdigit() == False:
            print('Número de páginas inválido, tente novamente')
            paginas = str(input("Quantidade de páginas do livro (Informe apenas o número): "))    
        Linha.append(paginas)
        escrita_livros.write(str(Linha))
        escrita_livros.write('\n')


def cadastro_emprestimo(matriz_usuarios, matriz_livrocad, dicionarios_emprestimo): #Função sobre emprestimos de livro
    with open('emprestimos.txt', 'a') as arq_escrita:
        dict_cadastro = {} 
        existe_cpf = -1
        CPF = str(input("Informe o CPF: "))
        while existe_cpf == -1:
            existe_cpf = percorrer(CPF, matriz_usuarios)
            if existe_cpf == -1:
                print("CPF não cadastrado. Retorne ao menu e faça o cadastro.")
                main()
            else:
                dict_cadastro['CPF'] = CPF
        ISBN = str(input("Informa o ISBN do livro: "))
        existe_isbn = -1
        while existe_isbn == -1:
            existe_isbn = percorrer(ISBN, matriz_livrocad)
            if existe_isbn == -1:
                print("ISBN não cadastrado. Retorne ao menu e faça o cadastro.")
                main()
            else:
                dict_cadastro['ISBN'] = ISBN
        retirada = str(input("Qual a data de retirada (dia/mês, Ex: dd/mm)? "))
        for dicionario in dicionarios_emprestimo:
            if CPF == dicionario['CPF'] and ISBN == dicionario['ISBN'] and retirada == dicionario['Data de retirada']:
                print("Não é permitido o cadastro duplicado de um empréstimo. Cadastre novamente.")
                cadastro_emprestimo(matriz_usuarios, matriz_livrocad, dicionarios_emprestimo)
        dict_cadastro['Data de retirada'] = retirada
        devolucao = int(retirada[3:])
        data_devolucao = 0
        if devolucao < 10:
            data_devolucao = f'{retirada[:-2]}0{devolucao + 1}'
        elif devolucao == 9:
            data_devolucao = f'{retirada[:-2]}10'
        elif devolucao == 10 or devolucao == 11:
            data_devolucao = f'{retirada[:-2]}{devolucao + 1}'
        elif devolucao == 12:
            data_devolucao = f'{retirada[:-2]}01'
        dict_cadastro['Data de devolução'] = data_devolucao
        dict_cadastro['Valor diário da multa por atraso'] = '5 reais'
        arq_escrita.write(str(dict_cadastro))
        arq_escrita.write('\n')
                    
#################################################################    FUNÇÕES PARA ALTERAR OS DADOS    #######################################################################################

#Função para alterar dados de um cadastro:
def alterar_user(matriz_usuarios, matriz_livroscad):
    print('Para alterar seu CPF, exclua e cadastre novamente')
    cpf = str(input("Informe o CPF do usuário que você deseja alterar: "))
    existe = percorrer(cpf, matriz_usuarios)
    if existe < 0:
        print("Usuário não encontrado.")
    else:
        alterar = str(input("Qual dado você deseja alterar: \n 1. Nome \n 2. Rua \n 3. Número \n 4. CEP \n 5. E-mail(s) \n 6. Telefone(s) \n 7. Data de nascimento \n 8. Profissão \n Opção: "))
        if alterar == '1':
            nome = str(input("Novo nome: "))
            matriz_usuarios[existe][1] = nome
        elif alterar == '2':
            Rua = str(input("Nova Rua: "))
            matriz_usuarios[existe][2] = Rua
        elif alterar == '3':
            Número = str(input("Novo número: "))
            matriz_usuarios[existe][3] = Número
        elif alterar == '4':
            CEP = str(input("Novo CEP: "))
            matriz_usuarios[existe][4] = CEP
        elif alterar == '5':
            editar_email(matriz_usuarios)
        elif alterar == '6':
            editar_telefone(matriz_usuarios)
        elif alterar == '7':
            nasc = str(input("Nova data de nascimento: "))
            matriz_usuarios[existe][7] = nasc   
        elif alterar == '8':
            profissao = str(input('Nova profissão: '))
            matriz_usuarios[existe][8] = profissao
        rewrite_user(matriz_usuarios)
    

#Função específica para editar email
def editar_email(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            for sublista in range(len(matriz[linha][5])):
                print(matriz[linha][5])
                email = int(input("Informe o número do e-mail que deseja alterar (ex: 1): "))
                email = email - 1
                novo_email = str(input("Novo e-mail: "))
                matriz[linha][5][email] = novo_email
                return matriz[linha][5][email]

#Função para editar telefones
def editar_telefone(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            for sublista in range(len(matriz[linha][6])):
                print(matriz[linha][6])
                telefone = int(input("Informe o número do telefone que deseja alterar (ex: digite '1' para o primeiro): "))
                telefone = telefone - 1
                novo_telefone = str(input("Novo telefone: "))
                matriz[linha][6][telefone] = novo_telefone
                return matriz[linha][6][telefone]
                
#Função para editar autor/a:
def editar_autor(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            for sublista in range(len(matriz[linha][3])):
                print(matriz[linha][3])
                autor = int(input("Informe o número do autor/a que deseja alterar (ex: 1): "))
                autor = autor - 1
                novo_autor= str(input("Novo autor/a: "))
                matriz[linha][3][autor] = novo_autor
                return matriz[linha][3][autor]

#Função para alterar dados de um livro:
def alterar_livro(matriz_livrocad,matriz_usuarios):
    print('Para alterar seu ISBN exclua e cadastre novamente')
    ISBN = str(input("Informe o ISBN do livro que você deseja alterar: "))
    existe = percorrer(ISBN, matriz_livrocad)
    if existe < 0:
        print("Livro não encontrado.")
    else:
        alterar = str(input("Qual dado você deseja alterar: \n 1. Título \n 2. Gênero \n 3. Autor \n 4. Número de Páginas \n Opção: "))
        if alterar == '1':
            Título = str(input("Novo Título: "))
            matriz_livrocad[existe][1] = Título
        elif alterar == '2':
            Gênero = str(input("Novo Gênero: "))
            matriz_livrocad[existe][2] = Gênero
        elif alterar == '3':
            editar_autor(matriz_livrocad)
        elif alterar == '4':
            Páginas = str(input("Novo número de páginas: "))
            matriz_livrocad[existe][4] = Páginas
        rewrite_livros(matriz_livrocad)

#Função para alterar dados de um empréstimo:
def alterar_emprestimo(matriz_usuarios, matriz_livrocad, dicionarios_emprestimo):
    print("Informe os dados para alterar a data de retirada")
    var = str(input("Informe o CPF: "))
    var2 = str(input("Informe o ISBN: "))
    for dicionario in dicionarios_emprestimo:
        if var == dicionario['CPF'] and var2 == dicionario['ISBN']:
            print(f"Consta um emprésimo nessa data {dicionario['Data de retirada']}")
            conferir = str(input("Deseja alterar essa data? Informe SIM ou NAO ")).lower()
            if conferir == 'sim':
                nova_data = input(str('Qual a nova data (dd/mm)?'))
                dicionario['Data de retirada'] = nova_data
                print('Alteração feita.')
                devolucao = int(nova_data[3:])
                data_devolucao = 0
                if devolucao < 10:
                    data_devolucao = f'{nova_data[:-2]}0{devolucao + 1}'
                elif devolucao == 9:
                    data_devolucao = f'{nova_data[:-2]}10'
                elif devolucao == 10 or devolucao == 11:
                    data_devolucao = f'{nova_data[:-2]}{devolucao + 1}'
                elif devolucao == 12:
                    data_devolucao = f'{nova_data[:-2]}01'
                dicionario['Data de devolução'] = data_devolucao
                rewrite_emp(dicionarios_emprestimo)
            else:
                print('Ok, alteração cancelada.')

#################################################################    FUNÇÕES PARA EXCLUIR DADOS    #######################################################################################

#Função para excluir usuários
def excluir_user(matriz_usuarios, matriz_livrocad): 
    var = str(input("Informe o CPF do usuário que deseja excluir: "))
    existe = percorrer(var, matriz_usuarios)
    if existe >= 0:
        print(matriz_usuarios[existe])
        x = input('Deseja mesmo excluir esse usuário? (S/s ou N/n): ').lower() #Confirmação após verificar dados
        if x == 's':
            del matriz_usuarios[existe]
            print("Dado excluído")
            escrita = open('usuarios.txt', 'w')
            rewrite_user(matriz_usuarios)
    else:
        print("Dado não consta em nosso sistema.")


#Função para excluir livros
def excluir_livro(matriz_livrocad,matriz_usuarios): #ALTERAR   
    var = str(input("Informe o ISBN do livro que deseja excluir: "))
    existe = percorrer(var, matriz_livrocad)
    if existe >= 0:
        print(matriz_livrocad[existe])
        x = input('Deseja mesmo excluir esse livro do sistema? (S/s ou N/n): ').lower() #Confirmação após verificar dados
        if x == 's':
            del matriz_livrocad[existe]
            print('Livro excluído do sistema')
            rewrite_livros(matriz_livrocad)
    else:
        print("Dado não consta em nosso sistema.")

#Função para excluir empréstimo
def excluir_emprestimo(matriz_usuarios, matriz_livrocad, dicionarios_emprestimo):
    existe = percorrer_arq(dicionarios_emprestimo)
    if existe >= 0:
        print(dicionarios_emprestimo[existe])
        x = input("Deseja excluir esse empréstimo do sistema? Digite S/s ou N/s: ").lower() #Confirmação após verificar dados
        if x == 's':
            del dicionarios_emprestimo[existe]
            print("Empréstimo excluído do sistema.")
            rewrite_emp(dicionarios_emprestimo)
    else:
        print("Dado não consta no sistema.")



######################################################################    FUNÇÕES PARA PERCORRER    #######################################################################################

#Função para verificar se já existe no arquivo texto
def percorrer(var, matriz):
    for i in range(len(matriz)):
        if matriz[i][0] == var:
            return i
    return -1 # o var não existe na matriz

def percorrer_arq(dicio):
    var1 = str(input("Informe o CPF: "))
    var2 = str(input("Informe o ISBN: "))
    var3 = str(input("Informe a data de retirada (dd/mm): "))
    for i in range(len(dicio)):
        print(i)
        indice = dicio[i]
        if var1 == indice['CPF'] and var2 == indice['ISBN'] and var3 == indice['Data de retirada']:
            return i
    return -1


################################################################ FUNÇÕES PARA PASSAR PARA O ARQUIVO ALTERAÇÕES OU EXCLUSÕES #############################################################

def rewrite_user(matriz):  
    escrita = open('usuarios.txt', 'w')
    for usuario in matriz:
        escrita.write(str(usuario))
        escrita.write('\n') 
    escrita.close()

def rewrite_livros(matriz):  
    escrita = open('livros.txt', 'w')
    for usuario in matriz:
        escrita.write(str(usuario))
        escrita.write('\n')         
    escrita.close()

def rewrite_emp(dicio):
    escrita = open('emprestimos.txt', 'w')
    for emp in dicio:
        escrita.write(str(emp))
        escrita.write('\n')
    escrita.close()


######################################################################## FUNÇÕES DOS RELATÓRIOS ########################################################################################

def relatorioA(matriz_usuarios):
    print("Relatório de usuários com a idade maior do que: ")
    matriz = []
    idade = int(input("Digite a idade em anos: "))
    for i in range(len(matriz_usuarios)):
        ano = matriz_usuarios[i][7]
        Ano = int(ano[-4:])
        idade_calculada = 2022 - Ano
        if idade_calculada > idade:
            matriz.append(matriz_usuarios[i])
    print(f"Os usuários com idade maior do que {idade} são: ")
    
    for linha in range(len(matriz)):
        print(f"{'*' * 25} \n CPF: {matriz[linha][0]} \n Nome: {matriz[linha][1]} \n Endereço: {matriz[linha][2]}, {matriz[linha][3]} \n CEP: {matriz[linha][4]} \n E-mail(s): {matriz[linha][5]} \n Telefone(s): {matriz[linha][6]} \n Data de nascimento: {matriz[linha][7]} \n Profissão: {matriz[linha][8]}")
        print('\n')

def relatorioB(matriz_livrocad):
    print("Relatório de livros com mais de x autores: ")
    matriz = []
    autores = int(input('Digite a quantidade de autores do livro: '))
    for i in range(len(matriz_livrocad)):
        num = len(matriz_livrocad[i][3])
        print(num)
        if num > autores:
            matriz.append(matriz_livrocad[i])
    print(f"Os livros com mais do que {autores} autores são: ")
    for linha in range(len(matriz)):
        print(f"{'*' * 25} \n ISBN: {matriz[linha][0]} \n Título: {matriz[linha][1]} \n Gênero: {matriz[linha][2]} \n Autores: {matriz[linha][3]} \n Número de páginas: {matriz[linha][4]}")
        print('\n')
   
def relatorioC(matriz_usuarios, matriz_livrocad, dicionarios_emprestimo):
    data_devolucao1 = str(input('Digite a primeira data de devolucao: '))
    data_devolucao2 = str(input('Digite a segunda data de devolucao: '))
    mesInt1 = int(data_devolucao1[-2:])
    mesInt2 = int(data_devolucao2[-2:])
    diaInt1 = int(data_devolucao1[:2])
    diaInt2 = int(data_devolucao2[:2])
    lista = []
    for i in range(len(dicionarios_emprestimo)):
        dicio = dicionarios_emprestimo[i]
        dia_devolucao = int(dicio['Data de devolução'][:2])
        mes_devolucao = int(dicio['Data de devolução'][-2:])
        if mesInt1 > mesInt2:
            if mesInt2 < mes_devolucao and mesInt1 > mes_devolucao:
                lista.append(dicio)
        elif mesInt1 < mesInt2:
            if mesInt1 < mes_devolucao and mesInt2 > mes_devolucao:
                lista.append(dicio)
        elif mesInt1 == mesInt2 and mes_devolucao == mesInt1:
            if diaInt1 > diaInt2:
                if diaInt2 < dia_devolucao and diaInt1 > dia_devolucao:
                    lista.append(dicio)
            elif diaInt2 > diaInt1:
                if diaInt1 < dia_devolucao and diaInt2 > dia_devolucao:
                    lista.append(dicio)

    print("Os empréstimos que estão entre as datas informadas são: ")
    for linha in lista:
        print('\n')
        print('*' * 25)
        print("CPF: ", linha['CPF'])
        CPF = linha['CPF']
        existe = percorrer(CPF, matriz_usuarios)
        print(f'Nome: {matriz_usuarios[existe][1]}')
        print("ISBN: ", linha['ISBN'])
        ISBN = linha['ISBN']
        existe2 = percorrer(ISBN, matriz_livrocad)
        print(f'Título do livro: {matriz_livrocad[existe2][1]}')
        print('Data de retirada:', linha['Data de retirada'], '\n' 'Data de devolução:', linha['Data de devolução'],'\n' 'Valor da multa:', linha['Valor diário da multa por atraso'])



############################################################################## MAIN ####################################################################################################

def main():
    print("==== Bem vindo. Iniciando sistema da biblioteca ====")

    matriz_usuarios = matriz_user()
    matriz_livrocad = matriz_livros()
    dicionarios_emprestimo = dicionarios()

    
    menu(matriz_usuarios, matriz_livrocad, dicionarios_emprestimo)

main()