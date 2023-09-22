def maiores(l, n):
    m=[]
    i=0
    while i<len(l):
        if l[i]>=n:
            m.append(l[i])
    	i = i + 1
        
    return sorted(m,key=int)

def acima_da_media(l):
    '''Função que dada uma lista com as notas dos alunos, retorna uma lista ordenada com as notas que ficaram acima da média; list->list'''
    media=sum(l)/len(l)    
    return maiores(l, media)
	if len(l)==1:
        return []