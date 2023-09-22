def acima_da_media(notas):
    ''' funcao que calcula e retorna a media dos alunos aprovados
list -> float, list'''
    media = sum(notas)/len(notas)
    aprovados = media(notas, media)
    return media, aprovados