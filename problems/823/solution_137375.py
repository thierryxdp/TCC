def faltante(pecas):
    """dada uma lista com numeros de 1 a N retorna qual numero consecutivo está faltando
    list-->int"""
    contador=0
    while contador<=len(pecas):
        contador=contador+1
        if contador not in pecas:
            return contador