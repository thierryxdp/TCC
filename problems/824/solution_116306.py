def uppCons(frase):
    posicao=0
    final=0
    while posicao<len(frase):
        if frase[posicao]not in 'AEIOUaeiou':
            final= final + frase.upper()
        posicao+=1
    return final