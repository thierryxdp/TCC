def posLetra(string, letra, n):
    """Recebe uma frase, uma letra e um numero. Retorna o índice da letra
    informada na sua n-ésima ocorrência na frase. Caso o número de ocorrências
    seja menor que n, retorna -1

    str, str, int -> int"""
    p = string.count(letra)
    i = 0
    k = 0
    indice=0
    if n > p:
        return -1
    else:
        while(i < n):
            if (string[k] == letra):
                i += 1
                indice = k
            k += 1
        return indice