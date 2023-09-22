def maiores(lis, n):
    '''Para cada elemento da lista l filtra apenas 
       os elementos maiores e iguais a n'''
    maiores_numeros = list()
    for c in lis:
        if c >= n:
            maiores_numeros.append(c)
            return maiores_numeros