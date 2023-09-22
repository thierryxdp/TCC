def repetidos(lista):
    ''' retorna o numero de vezes que um elemento da lista é igual ao elemento anterior, list->int'''
    i=1  
    rep=0
    while len(lista)>i:
        if lista[i]==lista[i-1]:  
            rep=rep+1 
            i=i+1 
        else:
            i=i+1 
    return rep