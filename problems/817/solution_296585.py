def acima_da_media (lista):
    '''
    	essa função recebe uma lista com as notas dos alunos de uma turna e retorna
        somente as notas que ficaram acima da média 
        list -> list
    '''
     media = sum(lista)//len(lista)
    
    if media in lista:
        lista.sort()
        x = lista.index(media)

        return lista[x+1:]
    
    elif media not in lista:
        lista.append(media)
        lista.sort()
        x = lista.index(media)

        return lista[x+1:]