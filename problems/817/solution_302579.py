def acima_da_media(notas_alunos):
    ''''''
    media=sum(notas_alunos)/len(notas_alunos)
    notas_alunos.append(media)
    list.sort(notas_alunos)
    x=notas_alunos.index(media)
    del(notas_alunos[:x+1]
    return notas_alunos