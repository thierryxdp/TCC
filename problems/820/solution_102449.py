def posLetra(string,letra,n):
    contador = 0
    S = string
    L = letra
    ordem = 0
    lista = []
    while ordem < str.count(S):
        if L == S[contador]:
            lista = lista + S[contador]
            ordem = ordem + 1
            contador = contador +1
        elif L != S[contador]:
            lista = lista + S[contador]
            contador = contador +1
    if ordem < n:
        return -1
    else:
        return len(lista)