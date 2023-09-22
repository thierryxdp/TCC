def acima_da_media(notas_alunos):
    ''''''
    media=sum(notas_alunos)/len(notas_alunos)
    notas_alunos.append(media)
    list.sort(notas_alunos)
    del(notas_alunos[:media+1]
    return notas_alunos