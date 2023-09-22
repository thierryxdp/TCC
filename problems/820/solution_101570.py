def posLetra (frase, letra, numero):
    """Função que retorna a ocorrência da letra na posição dada"""
    """str, str, int -> int"""
    i = 0
    n = 0
    while i<len(frase) and n < numero:
        if frase[i] == letra:
            n = n + 1
        i = i + 1
    if n < numero:
        return -1
    else:
        return i - 1