def repetidos(lista):
    '''retorna o numero de vezes que o
    elemento é igual ao elemento anterior
    list->int'''
    
    i=0
    q=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            q=q+1
        i=i+1
    return q