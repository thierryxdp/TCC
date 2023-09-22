def conta_numero(numero, matriz):
    """ Numero inteiro e uma matriz de inteiros retorna quantas vezes aparece o
    numero na matriz
    int-> int"""
    contador=0
    for lista_numerica in matriz:
        for num in lista_numerica:
            if num==numero:
                contador= contador + 1
    return contador