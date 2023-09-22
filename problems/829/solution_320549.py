def soma_h(n):
    '''Função que recebe o valor H com N termos e retorna o seu resultado com 2
    casas decimais, int -> float'''
    soma = 0
    for i in range(1,n+1):
        soma += (1/i)

    return round(soma, 2)