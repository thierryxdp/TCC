def posLetra(frase, letra, numero):
    ''' Funcao que recebe tres paramentos e retorna a ocorrencia de onde a letra esta
str, str, int -> int'''
    total = frase.count(letra)
    numero = int(numero)
    if (0 < numero <= total):
        posicao = -1
        while (numero > 0):
            posicao = frase.index(letra, posicao + 1)
            numero = numero - 1
        return posicao
    else:
        return -1