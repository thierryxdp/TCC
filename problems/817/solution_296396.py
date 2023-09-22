def acima_da_media(lista):
    ''' Calcular uma funcao que dada as notas dos alunos, retorne outra lista com as notas acima da media;
    list -> list'''
    
    media = (sum(lista))/len(lista)
    
    if media not in lista:
        list.append(lista, media)
        list.sort(lista)
        posicao = list.index(lista, media)
        return lista[posicao+1:]
    
    else:
        list.sort(lista)
        posicao = list.index(lista, media)
        return lista[posicao+1:]