# Questão 5
def acima_da_media(notas):
    """Função que retorne as notas acima da média;
    list -> list"""
    media = int(sum(notas)/len(notas))
    list.append(notas, media)
    list.sort(notas)
    indice = list.index(notas, media)
    return notas[indice + 1:]