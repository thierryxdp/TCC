def soma_h(n):
    '''função que calcula a soma de H com n termos, onde n é interno, retorna a soma com 2 casas decimais'''
    número = 0
    for i in range(1,n+1):
        número += (1/i)
    return round(número,2)