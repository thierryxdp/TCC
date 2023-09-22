def soma_h(N):
    '''Função que calcule e retorne o valor H com N termos onde N é inteiro,
       seu resultado deve retornar com 2 casas decimais, utilizando a função
       round(número, 2).
       int ---> float'''
    soma_parcial = 0
    for denominador in range(1,N+1):
        fracao = 1/denominador
        soma_parcial = soma_parcial + fracao
    return round(soma_parcial,2)