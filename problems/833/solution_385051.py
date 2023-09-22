def conta_numero(numero,matriz):
    """Retorna a quantidade de vezes que o número inteiro 
    inserido aparece na matriz;
    int, list -> int"""
    contador = 0
    for i in range(len(matriz)):
        contador = contador + list.count(matriz[i],numero)
    return contador