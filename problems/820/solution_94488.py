def posLetra(string,letra,numero):
    '''retorna em que posição da string a ocorrencia da letra esta. str,str,int->int'''
    lista=list(string)
    a=list.index(lista,letra)
    b=list.index(lista,letra,a+1)
    c=list.index(lista,letra,b+1)
    return c