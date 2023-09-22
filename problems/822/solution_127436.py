def repetidos(num):
    '''retorna o numero de vezes que o numero atual é igual o anterior. list -> int'''
    i = 0
    cont = 0
    while i<len(num):
        if num[i] == num[i-1]:
            cont = cont + 1
        i=i+1
        return cont