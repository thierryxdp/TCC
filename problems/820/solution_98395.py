def posLetra(frase, letra, n):
    '''Função que retorna a quantidade de "letra" de entrada: str, str, int -> int '''
    inicio = frase.find(letra)
    while inicio >= 0 and n > 1:
        inicio = frase.find(letra, inicio + 1)
        n -= 1 #n = n - 1
    return inicio