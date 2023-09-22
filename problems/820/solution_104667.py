def posLestra(texto,letra,n):
    '''funcao que retorna em que posicao da string a occorencia da letra esta
    str,str,int->int'''
    i=0
    lista=[]
    while i<len(texto):
        if letra == texto[i]:
            lista = lista+[i,]
            i=i+1
        if n>len(lista):
            return -1
        else:
            return lista[n-1]