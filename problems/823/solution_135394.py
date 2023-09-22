def faltante(listaN):
    '''
        Dada uma lista de N-1 numeros inteiros retorna qual elemento da lista está faltando.
        list -> int
    '''
    N = len(listaN)+1
    LP=list(range(1,N+1))
    i=0
    contador=[]
    while i<len(LP):
        if LP[i] not in listaN:
            contador = LP[i]
        i=i+1
    return contador