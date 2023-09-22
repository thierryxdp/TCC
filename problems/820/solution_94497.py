def posLetra(frase, letra, n):
    """funcao que retorna o indice da repeticao de numero n da letra
    informada na frase inserida
    
    str,str,int->int
    """
    i=0
    posicao=0
    while i<len(frase) and posicao < n:
        if letra in frase:
            list.index(list(frase,letra,posicao:))= posicao
            i=i+1
        return posicao
        else:
            return -1