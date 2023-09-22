def posLetra(frase,letra,n):
    """Funcao que retotna o indice de da repeticao de um numero n da letra informada na frase fornecida. str, str, int -> int"""
    l = 0
    o = 0
    while l < len(frase):
        if frase.count(letra) < n:
            return -1
        if frase[l] == letra:
            o = o + 1
            if o == n:
                return l
        l = l + 1