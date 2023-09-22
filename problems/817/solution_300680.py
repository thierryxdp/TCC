def acima_da_media(notas):
    '''calcula e retorna uma lista com as notas dos alunos que foram acima da média
    	list->list'''
    
    if len(notas)=1:
        media=sum(notas)/len(notas)
    	notas.append(media)
    	notas.sort()
    	m=notas.index(media)
    
    	return notas[m+2:]
    
    else: 
        media=sum(notas)/len(notas)
    	notas.append(media)
    	notas.sort()
    	m=notas.index(media)
    
    	return notas[m+1:]