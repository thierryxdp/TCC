def repetidos(l):
    '''Funcao que retorna numero de vezez que um elemento da lista 
    e igual ao elemento anterior
    entrada:tuple
    saida:int'''
    n=1
    cont=0
    while n<len(l):
        if l[n]==l[n-1]:
            cont+=1
        n+=1
    return cont