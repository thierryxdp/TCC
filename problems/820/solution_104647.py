def posLetra(frase,letra,n):
    '''1'''
    lista = []
    i = 0
    while i<len(frase):
        if frase[i]==letra:
            lista=lista+[i]
        if (len(lista)+1)<=n:
            v = -1
        if (len(lista)+1)>n:
            v= lista[n-1]
        i=i+1
    return v