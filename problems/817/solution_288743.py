acima_da_media(notas):
    """Recebe uma lista de notas de uma turma
    e retorna uma lista com aquelas notas maiores
    que a da média da turma
    list->list"""
    #Calcula a média com 2 casas decimais
    media_turma=round(sum(notas)/len(notas),1)
    #Inclui a média na lista de notas e ordena a lista
    notas.append(media_turma)
    notas.sort()
    #Determina onde a média aparecer pela 1a vez,
    #quantas vezes aparece e fatia a lista
    corte=notas.index(media_turma)
    contagem=notas.count(media_turma)
    return notas[corte+contagem:]