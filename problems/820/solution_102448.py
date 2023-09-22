def posLetra(string,letra,n):
    contador = 0
    S = string
    L = letra
    ordem = 0
    
    while contador < len(S):
        if L == S[contador]:
            ordem = ordem + 1
            contador = contador +1
        elif L != S[contador]:
            contador = contador +1
    if ordem < n:
        return -1
    else:
        return