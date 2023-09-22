def posLetra (string: str, letra: str , numero: int)-> int:
    ''' '''
    i = 0
    contador = 0
    while i < len(frase):
        if letra == frase[i]:
            contador = contador + 1
        if contador == n:
            return i
        i = i + 1
    return -1