from datetime import date
from time import sleep
    

mtitulo = ''
r = ''
data = str(date.today())
ano_atual = int(f'{data:.4s}')
mes = data[5:7]
dia = data[8:10]
databr = f'[{dia}/{mes}/{ano_atual}]'
tupla = 'Ramon', 1995
tupla2 = 'Ragnar', 1930
tupla3 = 'Radg', 1900
tupla4 = 'Sim', 1850
cadastro = [tupla, tupla2, tupla3, tupla4]


def titulo():
    global mtitulo, data
    a = 'AUTOESCOLA CESMAC'
    a2 = ('=' * 10 + a + '=' * 10)
    a3 = len(a2)
    a5 = ('=' * a3)
    mtitulo = f'{a5}\n{a2}\n{a5}'
    print(mtitulo)
    print('')
    print(databr)
    print('')


def tela_cadastro():
    global cadastro, r
    while r != 2:
        print('')
        r = input('Digite [1] para validar um novo candidato ou [2] para retornar ao menu. \nSua resposta: ')
        print('')
        if r.isnumeric() == True:
            r = int(r)
            if r == 1:
                ajuste = len('Digite o nome do candidato e sua data de nascimento:')
                ajuste = ajuste - (ajuste//2) - (len('[NOVA VALIDAÇÃO]') // 2)
                print('>' * ajuste, '[NOVA VALIDAÇÃO]', '<' * ajuste)
                print('Digite o nome do candidato e sua data de nascimento: ')
                print('')
                nome, nascimento = input('Nome: '), input('Ano de Nascimento: ')
                if nascimento.isnumeric() == True:
                    nascimento = int(nascimento)
                    idade = ano_atual - nascimento
                    candidato = nome, nascimento
                    cadastro.append(candidato)
                    if idade >= 18:
                        print('')
                        print(f'O candidato {nome} está aprovado para dar entrada em sua CNH, pois já atingiu a maioridade penal'
                              f' tendo {idade} anos de idade.')
                        sleep(2)
                    else:
                        print('')
                        print(f'Com a idade de {idade} anos, o candidato {nome} foi reprovado para a solicitação de CNH, pois ainda'
                              f' não atingiu a maioridade penal.')
                        sleep(2)
                else:
                    print('Valor digitado para nascimento é inválido! Tente novamente.')
            elif r == 2:
                print('Candidatos cadastrados nesta sessão: ')
                for i in cadastro:
                    print(cadastro.index(i)+1,i)
                print('')
                print('Retornando ao menu.')
                print('')
            if r != 1 and r != 2:
                print('Resposta inválida! Tente novamente.')
                sleep(2)
        else:
            print('A opção digitada é inválida; tente novamente.')
            print('')
            break


def principal():
    global cadastro
    titulo()
    while True:
        resp = input('Digite o número correspondente à opção desejada:\n'
                 '[1] Validar um novo candidato\n'
                 '[2] Consultar a lista de candidatos inseridos nesta sessão\n'
                 '[3] Excluir um candidato\n'
                 '[4] Sair do programa\n'
                 '\n'
                 'Digite sua opção: ')
        if resp == '1':
            tela_cadastro()
        if resp == '2':
            if len(cadastro) >= 1:
                print('')
                for i in cadastro:
                    print(cadastro.index(i)+1, i)
                print('')
                input(f'Pressione "Enter" para continuar.')
                print('')
            else:
                print('')
                print('Ainda não há candidatos cadastrados nesta sessão.')
                print('')
        if resp == '3':
            if len(cadastro) > 0:
                for i in cadastro:
                    print(cadastro.index(i)+1, 'º', i)
                print('')
                cadastropop = input('Escolha um cadastro a ser excluído digitando o número correspondente: ')
                if cadastropop.isnumeric() == True:
                    cadastropop = int(cadastropop)-1
                    if cadastropop > len(cadastro) or cadastropop < 0:
                        print('')
                        print('O número digitado não corresponde com os existentes em cadastro. Tente novamente.')
                        print('')
                    else:
                        cadastro.pop(cadastropop)
                        print('')
                        for i in cadastro:
                            print(cadastro.index(i)+1, i)
                print('')
            else:
                print('')
                print('Ainda não há candidatos cadastrados nesta sessão.')
                print('')
        if resp == '4':
            break
        if resp < '1' or resp > '4':
            print('')
            print('A opção digitada não é válida. Tente novamente.')
            sleep(1.5)
            print('')


principal()