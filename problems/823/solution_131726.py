def faltante(lista):
    """Esta função recebe uma lista de tamanho n-1 tendo números de 1 até n e diz qual número está faltando.
    list->int"""
    resultado = 0
    N = len(lista)+1
    for i in range(1,N+1):
        if i not in lista:
            resultado = i
        else:
            resultado = n 
    return resultado