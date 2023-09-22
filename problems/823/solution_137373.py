def faltante(pecas):
    """dada uma lista com numeros de 1 a N retorna qual numero consecutivo está faltando
    list-->int"""
    contador=1
    while contador<=len(pecas):
        if contador not in pecas:
            return contador
        contador=contador+1