def posLetra(frase,x, n):
    """funçao que recebe uma frase, uma letra x e a ocorrencia n desejada da letra na frase e retorna a posiçao da ocorrencia caso n seja menor que o numero de ocorrencias na frase retorna -1.
    entrada: str, str, int;
    saida: int."""
    i=0
    pos=0
    if str.count (frase, x) >= n:
        while frase[pos] != n :
            if x == frase [i]:
                i += 1
            pos += 1

        return i - 1
    else:
        return -1