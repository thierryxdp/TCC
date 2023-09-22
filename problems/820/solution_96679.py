def posLetra(frase,letra,indice):
    """ recebe uma string, uma letra e um indice(ocorrência) e decobre
    a posição da letra de acordo com o indice;str,str,int->int"""
    lista=str.split(frase)
    lista2=list.index(lista,letra)
    lista3=lista2[indice:]
    resposta=[]
    corredor=0
    return list.count(lista2,letra)