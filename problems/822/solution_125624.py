def repetidos(lista):
    '''retorna o numero de vezes que um elemento da lista é igual ao anterior;
    list->int'''
    x=0
    repe=0
    while x+1<len(lista):
        if lista[x]==lista[x+1]:
            repe=repe+1
        x=x+1    
    return repe