def acima_da_media(lista_notas:list) -> list:
    """Dada uma lista de notas de alunos, a função
    calcula e retorna uma lista com as notas que ficaram
    acima da média."""
    
    quant_notas = len(lista_notas)
    media = sum(lista_notas)/quant_notas
    
    list.append(lista_notas,media)
    list.sort(lista_notas)
    posicao_media = list.index(lista_notas,media)
    notas_acima_media = lista_notas[posicao_media+1:]
    
    if media in notas_acima_media:
        list.index(notas_acima_media,media)
    
    
    return notas_acima_media