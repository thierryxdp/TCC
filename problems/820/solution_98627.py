def posLetra(string:str, letra:str, numero:int)->int:
    posicao = 0
    while numero > 0:
        if string[posicao] == letra:
            numero -= 1
        posicao += 1
        if posicao == len(string):
            return -1
    return posicao