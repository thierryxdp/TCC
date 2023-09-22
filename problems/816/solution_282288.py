def maiores(lista,n):
    '''retorna uma nova lista com os numeros maiores que n em ordem crescente'''
    
    m = [x for x in lista if x > n]

    return m