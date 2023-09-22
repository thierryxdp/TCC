def conta_numero(numero,matriz):
    """Função que dado um numero e uma matrix, retorna quantas vezes esse número aparece na matrix. Entrada -> Int and Matrix; Saída -> int"""
    if numero in matriz:
        return matriz.count(numero)