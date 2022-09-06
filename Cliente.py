from socket import *
import PySimpleGUI as sg
from time import sleep


host = gethostbyname(gethostname())
port = 50000

#conexão com o servidor

client = socket(AF_INET, SOCK_STREAM)
client.connect((host, port))

#layout

soma = 0
saldo = 500
falha = 0
opcao = 0


def menu():
    global opcao, saldo
    sg.theme('DarkGrey2')
    layout=[
        [sg.Text('Clique na opção desejada:', size = (20, 2), font=16)],
        [sg.Button('Depositar', size = (30, 1), font=16)],
        [sg.Button('Sacar', size=(30, 1), font=16)],
        [sg.Button('Ver saldo', size=(30, 1), font=16)],
        [sg.Button('Sair')]
        ]

    menu = sg.Window('Eagle Bank', layout=layout, finalize= True)

    while True:
        eventos, valores = menu.read()
        if eventos == 'Sair' or sg.WINDOW_CLOSED:
            sg.popup('Finalizando...')
            break
        if eventos == 'Ver saldo':
            saldo = float(saldo)
            sg.popup(f'Seu saldo atual é: R${saldo:.2f}')
        if eventos == 'Depositar':
            opcao = 1
            client.send(str(opcao).encode())
            menu.hide()
            depositar()
            menu.un_hide()
        if eventos == 'Sacar':
            opcao = 2
            client.send(str(opcao).encode())
            menu.hide()
            sacar()
            menu.un_hide()


    menu.close()


def login():
    global soma
    sg.theme('DarkGrey2')
    layout = [
            [sg.Text('CPF', size = (11,1), font = 16)],
            [sg.InputText(key='login', font=10)],
            [sg.Text('Senha', size = (11, 1), font = 16)],
            [sg.InputText(key='senha', password_char= '*', font=10)],
            [sg.Button('Entrar'), sg.Button('Sair')]
            ]
    login = sg.Window('Eagle Bank', layout=layout, finalize=True)

    while True:
        eventos, valores = login.read()
        if eventos == 'Sair':
            sg.popup('Encerrando.')
            null = '0'
            client.send(null.encode())
            client.send(null.encode())
            break
        if eventos == 'Entrar':
            username = valores['login']
            password = valores['senha']
            client.send(username.encode())
            client.send(password.encode())
            msg = client.recv(1024).decode()
            if msg == 'Logado com sucesso':
                sg.popup('Autenticação concluída!')
                login.hide()
                menu()
                break
            elif msg != 'Logado com sucesso':
                sg.popup('Credenciais incorretas!')
                soma = soma + 1
            if soma == 3:
                sg.popup('Número de tentativas excedido. \n Finalizando...')
                sleep(1.5)
                client.close()
                break
    login.close()


def depositar():
    global saldo
    sg.theme('DarkGrey2')
    layout=[
        [sg.Text('Valor a ser depositado: ', size=(16,1), font=16)],
        [sg.InputText(key='valor', font=11)],
        [sg.Button('Confirmar'), sg.Button('Voltar')],
        ]

    depositar = sg.Window('Eagle Bank', layout=layout, finalize = True)

    while True:
        eventos, valores = depositar.read()
        if 'Confirmar':
            valor = valores['valor']
            client.send(valor.encode())
            valor = client.recv(1024).decode()
            valor = float(valor)
            saldo = valor
            sg.popup(f'Valor em conta atualizado: R${valor:.2f}')
            break
    depositar.close()


def sacar():
    global saldo, valor
    sg.theme('DarkGrey2')
    layout=[
        [sg.Text('Valor a ser sacado: ', size=(10,1), font=16)],
        [sg.Input(key='valor', font=11)],
        [sg.Button('Confirmar'), sg.Button('voltar')]
    ]

    sacar = sg.Window('Eagle Bank', layout=layout, finalize=True)

    while True:
        eventos, valores = sacar.read()
        if eventos == 'Confirmar':
            valor = valores['valor']
            client.send(valor.encode())
            print(saldo)
            saldo = client.recv(1024).decode()
            print(saldo)
            saldo = float(saldo)
            print(saldo)
            sg.popup(f'Seu saldo atualizado é de R${saldo}')
            break
        sacar.close()


#criar um bloco de leitura de eventos
login()

