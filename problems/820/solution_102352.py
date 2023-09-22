def posLetra(frase:str,letra:str,n:int) -> int:
    '''retorna a posição da n repetição da letra'''
    i = 0
    contador = 0
    while i < len(frase):
        if letra == frase[i]:
            contador+=1
        if contador == n:
            return i
        i+=1
    return -1