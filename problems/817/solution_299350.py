def acima_da_media(lista):
    '''Retorna uma lista com as notas acima da media da turma
    lista --> lista'''
    media = int(sum(lista)/len(lista))+1
    if(media in lista):
        list.sort(lista)
        maiores = lista[(list.index(lista,media)):] 
    else:
    	lista[0:0] = [media]
    	list.sort(lista)
    	maiores = lista[(list.index(lista,media))+1:]
    return maiores