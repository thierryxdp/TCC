def posLetra(frase, letra, n):
    """recebe como entrada uma string, uma letra, e um numero que indica a
ocorrencia desejada da letra"""
    i = 0
    contador = 0
    while i < len(frase):
        if letra == frase[i]:
            contador += 1
        if contador == n :
            return i
        i += 1
    return -1