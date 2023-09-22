def carros(pessoas, capacidade=5):
    '''retorna a quantidade de carros necessarios para certa quantidade de pessoas fazer uma viagem, caso os carros não tenham a capacidade normal de 5 pessoas, informar na segunda entrada'''
    x = pessoas / capacidade
    if int(x) % x == 0:
        a = 0
    elif int(x) == 0:
        a = 1
    else:
        a = 1
    return int(x) + a