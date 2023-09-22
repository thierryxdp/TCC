def acima_da_media(notas):
    """Função que retorna uma lista ordenada das notas acima da media
    list ->list"""
    a=notas
    media= sum(a)/len(a)
    if media not in a:
        list.append(a, media)
        a.sort()
        posmedia= list.index(a, media)
        return a[posmedia+1:]
    else:
        a.sort()
        posmedia= list.index(a,media)
        return a[posmedia+1:]