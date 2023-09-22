def posLetra(texto,letra,numero):
    '''A função retorna a posição da enesima ocorrência de uma letra em uma determinada frase.
    Ddos de entrada é uma string, uma letra (string) e um número inteiro, na saída ela devolve um número inteiro'''
    posicao = 0
    repeticao= 0
    for item in texto:
        if item == letra:
            repeticao+=1
        if numero == repeticao:
            break
        posicao+=1
    if repeticao != numero:
        return -1
    return posicao