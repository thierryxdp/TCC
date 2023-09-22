def posLetra(frase, letra, posicao):
    "Retorna a posição da letra na frase."
    i=0
    contador=0
    while i < len(frase):
        if letra == frase[i]:
            contador += 1
        if contador == posicao:
            return i
        i += 1
    return -1