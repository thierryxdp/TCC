def posicao_letra(textp,letra,n):
    i=0
    list=[]
    while i<len(texto):
        if letra==texto[i]:
            lista=lista+[i,]
            i=i+1
        if n>len(lista):
            return -1
        else:
            return lista[n-1]