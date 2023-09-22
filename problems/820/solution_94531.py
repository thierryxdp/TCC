def posLetra(string,letra,numero):
    '''retorna em que posicao da string a ocorrencia da letra esta.str,str,int->int'''
    lista=list(string)
    i=0
    l=[]
    if letra not in lista:
        return -1
    while i<len(lista):
        if lista[i]==letra:
            l=l+[i]
        i=i+1
    return l[numero-1]