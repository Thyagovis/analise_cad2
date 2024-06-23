import mysql.connector


conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    database = 'usuarios',
)

cursor = conexao.cursor()

usuarios = []
user_cad = {}

while True:

    op = int(input('''
1 - cadastrar usuários
2 - listar usuários
3 - sair
'''))
    
    if op == 1:

        usuario = input('Digite o nome do usuário: ')
        login_1 = input('Digite sua senha: ')
        login_2 = input('Confirme sua senha: ')

        if login_2 == login_1:

            comando = f'INSERT INTO usuarios_cad (nome, senha)  VALUES ("{usuario}", "{login_2}")'

            cursor.execute(comando)

    if op == 2:

        comando = 'SELECT * FROM usuarios_cad'
        cursor.execute(comando)

        dados = cursor.fetchall()
        for i in range(len(dados)):

            print(dados[i])

    if op == 3:

        break


            

    
