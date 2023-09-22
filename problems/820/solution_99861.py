def posLetra(frase, letra, n):
    """Recebe uma string, uma letra e o numero de ocorrencia e retorna
    a posição da string em que àquela ocorrência da letra occore;
    str, str, int -> int"""
    pos = -1
    if n <= frase.count(letra):
        i = 0
        while i < n:
            pos = frase.find(letra, pos + 1)
            i += 1
    return pos