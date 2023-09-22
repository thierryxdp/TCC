def acima_da_media(notas):
    """Função que retorna uma lista ordenada com as notas de entrada que ficaram
    acima da média. list-> list"""
    quant_notas = len(notas)
    media = sum(notas)/quant_notas
    list.append(notas,media)
    list.sort(notas)
    a3 = list.index(notas,media)
    return notas[a3+1:]