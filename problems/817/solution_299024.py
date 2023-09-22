def acima_da_media(notas):
    '''Função que dada uma lista com as notas dos alunos de uma turma, retorne uma lista ordenada com as notas que ficaram acima da média: list -> list'''
    media = sum(notas)/len(notas)
    list.append(notas,media)
    notas.sort()
    list.count(notas,media)
    if list.count(notas,media) == 1:
        list.index(notas,media)
        lista1 = notas[list.index(notas,media)+1:]
        return lista1
    if list.count(notas,media) > 1:
        list.index(notas,media)
        lista2 = notas[list.index(notas,media)+list.count(notas,media):]
        return lista2