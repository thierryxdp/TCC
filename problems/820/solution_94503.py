def posLetra(string,letra,n):
    """Funcao que retotna o indice de da repeticao de um numero n da letra informada na frase fornecida. str, str, int -> int"""
    l = 0
    i = 0
    while l < len(string):
        if string(l) == letra:
            if l == n:
                return l
            else:
                l += 1
        else:
            l += 1