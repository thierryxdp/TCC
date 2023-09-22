def repetidos(lista):
    '''retorna o numero de vezes que um elemento é igual ao elemento anterior'''
    '''list -> int'''
    
    r=0
    i=0
    
    for i in range(len(lista)-1):
        if lista[i] == (lista[i+1]):
            r = r = 1
        i = i +  1
        return r