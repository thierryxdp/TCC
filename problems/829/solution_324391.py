def soma_h(y):
    '''funcao que calcula e retorna o valor H com N termos onde N é inteiro e dado com entrada
    int->float'''
    acum = 0
    for i in range(1, y + 1):
        H = 1 / i
        acum += H 
    return round(acum, 2)