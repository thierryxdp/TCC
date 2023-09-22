def acima_da_media(lista):
    '''
    	Funcao que dada uma lista com notas de uma turma, retorne uma
        lista ordenada com as notas que ficaram acima da media 
    '''
    a= sum(lista)
    b= len(lista)
    c= a/b
    list.append(lista,c)
    list.sort(lista, reverse=True)
    d = list.index(lista,c)
    del lista[d:]
    list.sort(lista)
    return lista