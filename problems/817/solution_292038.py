#str->list
def acima_da_media(lista):
    "Função que dada uma lista com as notas dos alunos de uma turma, retorne uma lista ordenada com as notas que ficaram acima da da média."
    media_das_notas = sum(lista) / len(lista)
    list.append(lista,media_das_notas)
    list.sort(lista)
    posicao=list.index(lista,media_das_notas)
    lista=lista[:posicao:-1]
    if media_das_notas in lista:
        lista=lista[:posicao:-1]
    else:
        lista=lista[:posicao-1:-1]
    list.reverse(lista)
    return lista