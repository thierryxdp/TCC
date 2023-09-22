def faltante(lista):
    """função que calcula qual o número inteiro instá faltando no quebra cabeças,
    através da lista de entrada;
    Entrada: list
    Saída: int"""
    i = 0
    n = 1
    
    while i < len(lista):
        if lista[i] == n:
            n = n + 1
        i = i + 1
    return n