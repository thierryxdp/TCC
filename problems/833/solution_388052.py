def conta_numero(numero, matriz):
    """Função que dado um número inteiro e uma matriz de
    inteiros, conta e retorna quantas vezes aquele número
    aparece na matriz;
    int, list, list -> int"""
    lista = sum(matriz)
    return lista.count(numero)