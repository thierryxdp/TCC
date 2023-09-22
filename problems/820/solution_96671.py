def posLetra(frase,letra,indice):
    """ recebe uma string, uma letra e um indice(ocorrência) e decobre
    a posição da letra de acordo com o indice;str,str,int->int"""
    lista=str.split(frase)
    lista2=lista[indice:]
    resposta=[]
    corredor=0
    while(corredor<len(lista)):
        if indice< list.count(lista,letra):
            resposta+=[-1]
        else:
            resposta+=list.count(lista2,letra)
    return resposta