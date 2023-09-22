def faltante(N):
    ''' '''
    contador=0
    while contador < len(N):
        list.sort(N)
        contagem=list(range(1,N[-1]))
        if contagem[contador] not in N:
            return contagem[contador]
        contador=contador+1
        else N==list(range(1,N[-1])):
            return N[-1]+1