def acima_da_media(notas_alunos):
    x=sum(notas_alunos)
   	media=x/len(notas_alunos)
    notas_alunos.append(media)
    del(notas_alunos[:media+1]
    return notas_alunos