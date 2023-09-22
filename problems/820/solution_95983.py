def posLetra(frase,letra,n):
    '''str,str,int->'''
    posicao=str()
    i=0
    while i<len(frase):
        if letra == frase[i]:
            posicao=str(frase[i])
    return posicao