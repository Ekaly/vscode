from socket import *

host = gethostbyname(gethostname())
port = 50000

print(f'Servidor conectado ao host {host}, port {port}')

servidor = socket(AF_INET, SOCK_STREAM)
servidor.bind((host, port))
servidor.listen(1)

con, adr = servidor.accept()
print(f'Cliente {adr} se conectou ao servidor')

logado = False
opcao = 0
valor = 0
saldo = 500
falha = ''
formato = 'utf-8'


# validação de login

def auth():
    soma = 0
    logado = False
    while True:
        login = con.recv(1024).decode()
        senha = con.recv(1024).decode()
        print (login, senha)
        print (soma)
        if login == '0' and senha == '0':
            servidor.close()
            break
        if (login == 'teste' and senha == 'teste'):
            sucesso = ('Logado com sucesso')
            con.send(sucesso.encode())
            break
        if soma < 3:
            if (login != 'teste' or senha != 'teste'):
                falha = 'falha'
                con.send(falha.encode())
                soma = soma + 1
        elif soma == 3:
            break
        else:
            falha = 'falha'
            soma = soma + 1
            break


def menu():
    auth()
    global opcao, falha, saldo, valor
    while True:
        opcao = con.recv(1024).decode()
        opcao = int(opcao)
        print(opcao)

        if opcao == 1:
            valor = con.recv(1024).decode()
            valor = float(valor)
            saldo = saldo + valor
            con.send(str(saldo).encode())
        elif opcao == 2:
            saldo = con.recv(1024).decode()
            saldo = float(valor)
            falha = saldo - valor
            print (falha)
            con.send(str(falha).encode())
            if falha >= 0:
                saldo = falha
                con.send(str(saldo).encode())
            else:
                con.send(str(falha).encode())
        elif opcao == 3:
            servidor.close()
            break


menu()