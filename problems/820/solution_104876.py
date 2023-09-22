def posLetra(texto,letra,n):
    '''funcao que tem como entrada uma string, e retorna a posicao em que esta a string;
    str,str,int->int'''
    i=0
    lista=[]
    while i<len(texto):
        if letra == texto[i]:
            lista=lista+[i,]
            i=i+1
    if n>len(lista):
        return -1
    else:
        return lista[n-1]