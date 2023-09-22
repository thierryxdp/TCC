def posLetra(palavra, letra, n):
    '''função que recebe uma string, uma letra e um número que indica a posição desejada da letra. Ela retorna a posicção que em a letra dentro da string está'''
    proximo = 0
    acumulador = 0
    while proximo < len(palavra):
        if letra == palavra[proximo]:
            acumulador = acumulador + 1
        if acumulador == n:
            return proximo
        proximo = proximo +1
    return -1