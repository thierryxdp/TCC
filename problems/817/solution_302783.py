def acima_da_media(notas_alunos):
    
    media=sum(notas_alunos)/len(notas_alunos)
    notas_alunos.append(media)
    list.sort(notas_alunos)
    x=notas_alunos.index(media)
    
    if media not in notas_alunos:
        del(notas_alunos[:x+1])
    else:
        notas_aluns=[]
    return notas_alunos