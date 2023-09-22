def conta_numero(numero, matriz):
    """ Retorna quantas vezes o numero dado aparece na matriz dada;
        Entrada: int, list;
        Saida: int;
     """
    resultado = 0
    for numero in matriz:
        resultado += numero
    return resultado