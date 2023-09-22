def posLetra(frase,letra,indice):
    '''função que a partir de uma frase, uma letra e um indice da ocorrencia dessa letra devolve em qual indice a ocorrencia pedida dessa letra aparece;str,str,int->int'''
    j=0
    o=''
    if str.count(frase,letra)<indice:
        return -1
    while j<len(frase):
        if len(o)==indice:
            return j-1
        elif frase[j]==letra:
            o=o+letra
        j=j+1