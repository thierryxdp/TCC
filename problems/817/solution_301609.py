def maiores(ls,n):
    list.append(ls,n)
    list.sort(ls)
    pos=list.index(ls,n)     
	return ls[pos+1:]

def acima_da_media(ls):
    '''Função que, dada uma lista com as notas dos alunos de uma turma,
    retorna uma lista ordenada com as notas que ficaram acima da
    média.
    assinatura: list -> list '''
    media=sum(ls)/len(ls)
	if(media == sum(ls)):
		return[]    
    return maiores(ls,media)