def conta_numero(numero,matriz):
    """função que calcula e retorna quantas vezes um número inteiro aparece na matriz,
    através dos dados de entrada numero e matriz;
    Entrada: int, list
    Saída: int"""
    
    for elemento in matriz:
        x = str.find(matriz[numero], numero)
    return numero