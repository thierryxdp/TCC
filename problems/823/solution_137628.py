def faltante(numeros):
    """Funcao que dada uma lista de numeros N de tamanho N-1
    retorna o numero da sequencia que esta faltando
    list -->int"""
    i = 0
    ultimo_numero = numeros[-1]
    while i < (len(numeros)+1):
        if ultimo_numero != len(numeros):
            if i != 0:
                if i not in numeros:
                    return i
        if ultimo_numero == len(numeros):
            return ultimo_numero + 1
        i = i + 1