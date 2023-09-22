def faltante(lista):
    '''Esta função que dada uma lista, descubra qual numero inteiro 
    desse intervalo esta faltando 
    lit >>> int '''
    i=0
    n=0
    lista = sorted(lista)
    if lista[0]!=1:
        return 1
    
    while i < len(lista)-1:
    if lista[i+1]! = lista[i]+1:
            return lista[i] + 1
        
        i+=1
    return lista[i]+1