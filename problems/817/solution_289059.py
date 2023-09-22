def acima_da_media (notas):
    """Função que, dada uma lista com notas, retorna uma lista ordenada com as notas que ficaram acima da media
    Entrada: lista[int]
    Saída: lista[int]"""
    
    media = sum(notas) / len(notas)
    list.append(notas, media)
    list.sort(notas)
    posicao = list.index(notas, media)
    del notas[:posicao+1]
    if media in notas:
        list.remove(notas, media)
        return notas
    else:
        return notas