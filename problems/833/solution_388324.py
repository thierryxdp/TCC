def conta_numero(numero,matriz):
    """
    Essa função retorna a quantidade de vezes que um 
    determinado número aparece em uma matriz
    Parametro de Entrada: int, list
    Valor de Retorno: int
    """
    contador = 0
    for i in matriz:
        for k in i:
            if numero == k:
                contador = contador + 1
    return contador