def faltante(lista):
    """Esta função recebe uma lista de tamanho n-1 tendo números de 1 até n e diz qual número está faltando.
    list->int"""
    resultado = 0
    n = len(lista)
    for i in range(1,n+1):
        if i not in lista:
            resultado = i
    return resultado