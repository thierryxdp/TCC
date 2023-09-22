def posLetra(palavra,letra,n):
    '''retorna em que posição da palavra aquela ocorrência da letra está;
str,str,int->int'''
    i=0
    lista=[]


    while i<len(palavra):
        if palavra[i] == letra:
            lista= lista + [i]
        i=i+1

    if len(lista) < n:
            return -1
        
    return lista[n-1]