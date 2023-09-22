def faltante(numeros):
    """Funcao que dada uma lista de numeros N de tamanho N-1
    retorna o numero da sequencia que esta faltando
    list -->int"""
    i = 0
    while i < len(numeros):
        if i != 0:
            if i not in numeros:
                return i
            if i in numeros:
                return i + 1
        i = i + 1