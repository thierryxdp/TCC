def acima_da_media(lista):
    '''Função que recebe uma lista de entrada contendo as notas 
    de alunos, e retorna uma nova lista, contendo as notas acima da média'''
    ''' list -> list'''
    #Casos de teste:
    ''' acima_da_media([1,2,2,1,4,9,9,8,8,10])
    -> [8, 8, 9, 9, 10]
        acima_da_media([2,2,2,8,8,10,5,5.9])
    -> [5.9, 8, 8, 10]
        acima_da_media([9,10,10,10,10])
    -> [10, 10, 10, 10] '''
    media = int(sum(lista)/len(lista))
    lista.append(media)
    lista.sort()
    indiceMedia=lista.index(media)
    Nlist=lista[indiceMedia+1:].copy()
    if media in Nlist:
        del Nlist[0]
    return Nlist