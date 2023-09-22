def acima_da_media (notas):
    '''função que dada uma lista com as notas do alunos de uma turma, retorna uma lista ordenada com as notas que
    ficaram acima da média.
    list -> list'''
    
    media = sum(notas)/len(notas)
    
    if media in notas:
        list.sort(notas)
        posicao = list.index(notas, media)
        return notas[posicao+1:]
    else:
        list.append(notas, media)
    	list.sort(notas)
    	posicao = list.index(notas, media)
    	return notas[posicao+1:]