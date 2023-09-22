def acima_da_media(notas):
    '''recebe as notas de alunos de uma sala em lista
    e retorna uma lista com as notas daqueles acima da media
    list -> list'''
   
    import math
    
    media = sum(notas)/len(notas)
    
    list.append(notas , media)
    
    list.sort(notas)
	
    if notas[list.index(notas,media)+1] == media:
    	novalista = notas[list.index(notas , media)+2:]
	else:
        novalista = notas[list.index(notas , media)+1:]
    
    return novalista