def conta_numero(n,X):
    """Função que dao um número inteiro e uma matriz de inteiros, retorna e conta quantas vezes aquele número aparece"""
    contador=0
    for i in X:
        for j in i:
            if n==j:
                contador=contador+1
    return contador