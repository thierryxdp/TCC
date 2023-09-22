def repetidos(num):
    '''retorna o numero de vezes que o numero atual é igual o anterior. list -> int'''
    i = 0
    cont = 0
    while i<len(num):
        j=i-1
        if num[j] is num[i]:
            cont = cont + 1
        i=i+1
        return cont