def acima_da_media(notas):
    """Função que dada uma lista com as notas dos alunos
    de uma turma, retorna uma lista ordenada com as notas acima
    da média;
    list -> list"""
    media=sum(notas)/len(notas)
    i=list.index(notas,media)
    list.append(media)
    list.sort(media)
    return notas[i+1:]