def soma_h(n):
    '''função que dado um número n inteiro, retorna o valor de
    H com n termos'''
    soma=0
    for t in range(1,n+1):
        inverso = 1/t
        soma += inverso
     return round (soma,2)