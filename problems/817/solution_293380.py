# Questão 5
def acima_da_media(notas):
    """Função que retorne as notas acima da média;
    list -> list"""
    media = sum(notas)/int(len(notas))
    list.append(notas, media)
    list.sort(notas)
    indice = list.index(notas, media)
    return notas[indice + 1:]