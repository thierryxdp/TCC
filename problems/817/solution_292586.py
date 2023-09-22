def acima_da_media(notas):
    '''Recebe uma lista com as notas de uma turma de alunos e retorna uma lista contendo apenas aquelas acima da media das notas'''
    #list -> list
    media = sum(notas)/len(notas)
    list.append(notas, media)
    list.sort(notas)
    indice = list.index(notas, media)
    return notas[indice + 1:]