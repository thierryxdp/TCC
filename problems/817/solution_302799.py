def acima_da_media (lista):
    """Função que dada uma lista com notas, retorna apenas as notas acima da média.
    list-> list"""
acima_med = []
    for numeros in lista:
        if numeros >= 5:
            acima_med(numeros)
    return sorted(acima_med)