def repetidos(lista):
    """calculo e retorno de quantas vezes um elemento da lista é igaul ao elemento anterior"""
    k=[]
    i=1
    while i<len(lista):
        if lista[i]==lista[i-1]:
            k=k+[lista[i]]
        i=i+1
    return len(k)