def acima_da_media(notas):
    ''' funcao que calcula a media de uma turma e retorna a media e aprovados
int ->int'''
    media = sum(notas)/len(notas)
    aprovados = media(notas, media)
    return media, aprovados