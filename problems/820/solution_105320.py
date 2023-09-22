def posLetra(texto,letra,numero):
    '''retorna o número de ocorrencia de uma letra dada a posição no texto'''
    if 0 < numero <= texto.count(letra):
        i = 0
        while numero > 0:
            i = texto.find(letra, i)
            numero-=1
        return i
    return -1