'''Recebe uma lista com as notas de uma turma de alunos e retorna uma lista contendo apenas aquelas acima da media das notas'''
#list -> list
def acima_da_media(notas):
    media = sum(notas)/len(notas)
    round(media,0)
    list.append(notas, media)
    list.sort(notas)
    indice = list.index(notas, media)
    return notas[indice + 1:]