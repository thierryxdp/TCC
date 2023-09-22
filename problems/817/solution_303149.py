def acima_da_media(notas):
    """Determinar uma lista de notas crescente com todas notas acima de 7;
    list - > list"""
    media = sum(notas)/len(notas)
    if media in notas:
        notas.remove(media)
    return maiores(notas,media)