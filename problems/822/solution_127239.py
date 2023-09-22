def repetidos(lista):
    '''retorna quantas vezes um numero é igual ao anterior.
    lista->int'''
    i=1
    vezes=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            vezes+=1
        i+=1
    return vezes