def filtraMultiplos(lista,numero):
    """funcao que, dada uma lista com numeros inteiros e um numero inteiro como parametro, retorna uma lista com todos os numeros da lista que sao multiplos de do numero inteiro dado como entrada
    list(int),int--->list(int)"""
    i=0
    listaFinal=[]
    while i<len(lista):
        if lista[i]%numero==0:
            listaFinal=listaFinal+[lista[i]]
        i=i+1
    return listaFinal