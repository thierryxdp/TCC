def acima_da_media(lista):
    
    media=sum(lista)/len(lista)
    local=list.index(lista,media)
    for i in lista:
    	if(i<media):
        	return lista[:local]