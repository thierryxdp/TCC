def soma_h(N):
    '''Função que calcule e retorne o valor H com N termos onde N é inteiro,
       seu resultado deve retornar com 2 casas decimais, utilizando a função
       round(número, 2).
       int ---> float'''
    soma_parcial = 0
    denominadores = range(1,N+1)
    for denominador in range(1,N+1):
        #numerador = 2 * denominador - 1
        fração = 1/denominador
        soma_parcial = soma_parcial + fração
    return soma_parcial