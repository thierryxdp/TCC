def acima_da_media(notas):
    '''recebe as notas de alunos de uma sala em lista
    e retorna uma lista com as notas daqueles acima da media
    list -> list'''
   
    import math
    
    media = mat.ceil(sum(notas)/len(notas))
    
    list.append(notas , media)
    
    list.sort(notas)
	
    if int(media) in notas:
    	novalista = notas[list.index(notas , media)+2:]
	else:
        novalista = notas[list.index(notas , media)+1:]
    
    return novalista