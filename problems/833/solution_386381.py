def conta_numero(numero,matriz):
    """retorna quantas vezes um número aparece na matriz (int, list -> int)"""
    soma = 0
    for i in range(len(matriz)):
        for j in (matriz[i]):
            if j == numero:
                soma = soma + 1 
    return soma