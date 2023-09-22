# Questão 5
def acima_da_media(notas):
    """Função que retorne as notas acima da média;
    list -> list"""
    media = sum(notas)/len(notas)
    list.append(notas, media)
    list.sort(notas)
    indice = list.index(notas, media)
    lista_nova = notas[indice + 1:]
    if media == lista_nova[0]:
        list.pop(lista_nova, 0)
        return lista_nova
    else:
        return lista_nova