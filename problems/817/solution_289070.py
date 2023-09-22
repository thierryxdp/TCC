def acima_da_media(lista):
    '''função que ordena e retorna uma lista de notas de alunos acima da média a partir de uma lista recebida contendo todas as notas; list -> list'''
    
    media = sum(lista)//len(lista)
    lista.append(media)
    lista.sort()
    a = lista.index(media)
    
    if media in lista:
        return lista[a+2:]
    
    elif media not in lista:
        return lista[a:]