def acima_da_media(lista_notas):
    '''
    	Funcao que dada uma lista com notas de uma turma, retorne uma
        lista ordenada com as notas que ficaram acima da media 
    '''
    L = lista_notas
    list.sort(L)
    del L[0:(len[L]/2)]
    return L