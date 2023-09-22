def faltante(numeros):
    """Funcao que dada uma lista de numeros N de tamanho N-1
    retorna o numero da sequencia que esta faltando
    list -->int"""
    i = 0
    while i < (len(numeros)+1):
        if i != 0:
            if i not in numeros:
                return i
        i = i + 1