def posLetra(frase,letra,ocorrencia):
    '''Esta função retorna o índice de uma letra dados uma palavra, a letra desejada e a ocorrência.
str,str,int->int'''
    i=0
    while i<len(frase):
        if frase.count(letra)<ocorrencia:
            return -1
        elif ocorrencia==1:
            indice=str.index(frase,letra)
            return indice
        else:
            str.replace(frase,letra,'Z',ocorrencia-1)
            b=str.index(frase,letra)
            return b
        i=i+1