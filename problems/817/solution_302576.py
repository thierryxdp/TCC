def acima_da_media(notas_alunos):
    list.sort(notas_alunos)
    media=sum(notas_alunos)/len(notas_alunos)
    notas_alunos.append(media)
     
    return notas_alunos