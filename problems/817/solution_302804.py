def acima_da_media (lista):
    """Função que dada uma lista com notas, retorna apenas as notas acima da média.
    list-> list"""
    acima_med = []
    media == [sum(lista)/len(lista)]
    for notas in lista:
        if notas >= media:
            acima_med.append(notas)
    return sorted(acima_med)