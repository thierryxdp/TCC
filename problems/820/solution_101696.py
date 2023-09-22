def posLetra(frase, letra, n):
    """Função que retorna a posição de uma letra, dado o número de ocorrências que essa letra aparece na frase"""
    """str, str, int -> int"""
    i = 0
    contador = 0
    while i < len(frase):
        if frase[i] == letra:
            contador = contador + 1
            if contador == n:
                return i
        elif i == len(frase) and contador != n:
            return -1
        i = i + 1