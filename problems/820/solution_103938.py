def posLetra(frase,letra,posi):
    i=0
    posicao=0
    while i<frase:
        if letra in frase[i]:
            posicao=posicao+1
        if posi==posicao:
            return i
        i=i+1