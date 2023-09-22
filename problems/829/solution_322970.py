def soma_h(N):
    '''calcular e retornar o valor H com N termos onde N é inteiro e dado com entrada.(H=1+1/2+1/3+...+1/N) 
    Retorne seu resultado somente com 2 casas decimais, utilizando a função
    int->float'''
    valor = 0
    for x in range(1, N + 1):
        valor += 1 / x
    return round(valor, 2)