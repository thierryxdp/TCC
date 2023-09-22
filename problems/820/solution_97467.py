def posLetra(frase,l,n):
    """Função que recebe uma frase e retona a posição da letra l
    na ocorrencia n, se não houver aquele numero de ocorrencias da letra
    será retornado -1"""

    i = 0
    if l in frase:
        while i < len(frase) - 1:
            if l == frase[i]:
                n = n-1
                i = i+1
            if l != frase[i]:
                i = i+1
            if n == 0:
                return i - 2
            
    return -1