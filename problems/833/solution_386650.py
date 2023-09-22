def conta_numero(numero,matriz):
    """Função que dado um numero e uma matrix, retorna quantas vezes esse número aparece na matrix. Entrada -> Int and Matrix; Saída -> int"""
    linha = len(matriz)
    coluna = len(matriz[0])
    for numero in linha or numero in coluna:
        return matriz.count(numero)