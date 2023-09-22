def repetidos(lista):
    ''' função que recebe uma lista de números e define quantas
    	vezes um número é igual ao elemnto anterior.
        list ---> int '''
    a = 0
    b = 0
    while a < len(lista):
        if lista[a] == lista[a-1]:
            b = b + 1
            a += 1
        else:
            a += 1
            
    return b