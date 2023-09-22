def acima_da_media(notas):
    '''com'''
    media=sum(notas)/len(notas)
    funcao= [notas]+[media]
    list.sort(notas)
    media=list(media)
    if notas>=media:
    	return funcao