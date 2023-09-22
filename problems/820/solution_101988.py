def posLetra(frase,letra,ocorrencia):
    '''Retorna em que posição da frase a ocorrência da letra está
str,str,int -> int'''
    if str.count(frase,letra)<ocorrencia:
        return -1
    else:
        novafrase=str.replace(frase,letra,'#',ocorrencia-1)
        return str.index(novafrase,letra)