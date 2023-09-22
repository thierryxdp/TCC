def acima_da_media(notas):
    """recebe conjunto de notas e retorna novo conjunto com notas acima da media
    entrada: list
    saida: list"""
    soma=sum(notas,1)
    l=len(notas)
    media=soma/l
    if len(notas)>=2:
        list.append(notas,media)
        list.sort(notas)
        objeto=list.index(notas,media)
        notas=notas[objeto+1:]
        return notas
    else:
        return []