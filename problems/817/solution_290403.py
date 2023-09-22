def acima_da_media(notas):
    media=sum(notas)/len(notas)
    if media in notas:
        list.sort(notas)
    	index=list.index(notas,media)
    	return notas[index+1:]    
    list.append(notas,media)
    list.sort(notas)
    index=list.index(notas,media)
    return notas[index+1:]