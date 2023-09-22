def acima_da_media(notas):
    """Função que retorna uma lista ordenada com as notas de entrada que ficaram
    acima da média. list-> list"""
    quant_notas = len(notas)
    media = sum(notas)/quant_notas
    a1 = list.append(notas,media)
    a2 = list.sort(a1)
    a3 = list.index(a2,media)
    return a2[a3+1:]