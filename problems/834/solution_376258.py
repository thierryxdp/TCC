def media_matriz(M):
    """dada uma matriz de inteiros de tamanho qualquer, função retorna a média
    de todos os numeros da matriz. List -> Float"""
    
    soma = 0
    n_total = 0

    for i in M:
        soma += sum(i)
        n_total += len(i)

    return soma / n_total