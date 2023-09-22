def posLetra(string:str,letra:str,numero:int):
    posicao=0
    frase=string
    while posicao<len(string):
        if letra in string:
            frase=frase.count(letra)
            posicao=posicao+1
    return frase