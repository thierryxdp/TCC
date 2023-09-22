def acima_da_media(notas):
    '''Dado uma lista com as notas dos alunos, retorna os alunos acima da media
    da turma;
    list-> list'''
    media=round(sum(notas)/len(notas))
    list.append(notas,media)
    if media in notas:
        list.sort (notas)
    	x=list.index(notas,media)
        list.remove (notas,media)
    	return notas[x+1:]
    else:
        list.sort (notas)
    	x=list.index(notas,media)
    	return notas[x+1:]