def carros(pessoas, capacidade=5):
    '''retorna a quantidade de carros necessarios para certa quantidade de pessoas fazer uma viagem, caso os carros não tenham a capacidade normal de 5 pessoas, informar na segunda entrada'''
    x = pessoas / capacidade
    return ceil(x)