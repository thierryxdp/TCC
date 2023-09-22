def posLetra(frase,letra,n):
    '''funcao que retorna em qual posicao da frase a letra se repete em relacao ao numero dado
    str,str,int->int'''
    ordem=frase.index(letra)
    while ordem>=0 and n>1:
        if letra!=frase:
            return -1
        ordem=frase.index(letra,ordem+1)
        n=n-1
    return ordem