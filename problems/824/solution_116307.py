def uppCons(frase):
    posicao=0
    
    while posicao<len(frase):
        if frase[posicao]not in 'AEIOUaeiou':
            final= frase.upper()
        posicao+=1
    return final