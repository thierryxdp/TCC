def filtra_pares(a,b,c,d):
    X = a,b,c,d
    resposta = filter(X % 2,filtra_pares)
    return resposta