def posLetra(frase,letra,n):
    """Função que retorna a posição de uma letra, dada a frase, a letra, e a ocorrência desejada."""
    """String, String, int -> Int"""
    i = 0
    j = 0
    while i < len(frase) and j != n:
        i = i + 1
        if frase[i] == letra:
            j = j + 1
            if j  == n:
                return i
    return -1