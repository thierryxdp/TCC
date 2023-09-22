def posLetra(texto,letra,n):
    """funcao que tem como entrada uma string, e regorna em que posição esta a string da letra;
    str->list"""
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