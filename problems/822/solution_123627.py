def repetidos (lista):
    '''retorna quantos numeros seguidos sao iguais na lista
    do 1 arg
    list -> int'''
    i = 0 #contador
    j = 0 #acumuluador
    
    while 0 < i < len(lista):
        if lista[i] == lista[i-1]:
            j = j + 1
    i = i + 1
    
    return j