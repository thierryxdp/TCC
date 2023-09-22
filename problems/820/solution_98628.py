def posLetra(string:str, letra:str, numero:int)->int:
    posicao = -1
    while numero > 0:
        posicao += 1
        if posicao == len(string):
            return -1
        elif string[posicao] == letra:
            numero -= 1
    return posicao