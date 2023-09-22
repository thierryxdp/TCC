def acima_da_media (lista):
    """Função que dada uma lista com notas, retorna apenas as notas acima da média.
    list-> list"""
    acima_med = []
    for notas in lista:
        if notas >= 5:
            acima_med.append(notas)
    return sorted(acima_med)