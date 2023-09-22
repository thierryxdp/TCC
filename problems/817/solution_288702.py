def acima_da_media(notas):
    """Recebe uma lista de notas de uma turma
    e retorna uma lista com aquelas notas maiores
    que a da média da turma
    list->list"""
    media_turma=round(sum(notas)/len(notas),2)
    lista_acima_media=[]
    for m in range(len(notas)):
        if notas[m]>media_turma:
            lista_acima_media=lista_acima_media+[notas[m]]
    lista_acima_media.sort()
    return lista_acima_media