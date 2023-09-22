def faltante(N):
    ''' '''
    contador=0
    while contador < len(N):
        list.sort(N)
        contagem=list(range(1,N[-1]))
        if contagem[contador] not in N:
            return contagem[contador]
         if N==list(range(1,N[-1])):
            return N[-1]+1
        contador=contador+1