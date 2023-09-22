def acima_da_media(notas):
    '''Função que dada uma lista com as notas dos alunos de uma turma, retorne uma lista ordenada com as notas que ficaram acima da média: list -> list'''
    media = sum(notas)/len(notas)
    list.append(notas,media)
    notas.sort()
    list.index(notas,media)
    lista1 = notas[list.index(notas,media):]
    return lista1