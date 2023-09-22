def acima_da_media(lista):
    '''função que ordena e retorna uma lista de notas de alunos acima da média a partir de uma lista recebida contendo todas as notas; list -> list'''
    
    media = sum(lista)//len(lista)
    lista.sort()
    a = lista.index(media)
    
    if media in lista:
        
        return lista[a+1:]
    
    elif media not in lista:
        lista.append(media)
        return lista[a+1:]