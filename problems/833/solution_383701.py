def conta_numero(numero,matriz):
    """função que calcula e retorna quantas vezes um número inteiro aparece na matriz,
    através dos dados de entrada numero e matriz;
    Entrada: int, list
    Saída: int"""
    resultado = 0
    
    for indice in range(len(matriz)):
        x = list.count(matriz[indice], numero)
        resultado = resultado + x
    return resultado