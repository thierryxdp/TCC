def acima_da_media(lista_n):
    '''
    Funçao que dada uma lista com as notas doa alunos de uma turma,
    retorna uma lista ordenada com as notas acima da media
    list-> list
    '''
    media= sum(lista_n)/len(lista_n)
    
    list.append(lista_n, media)
    list.sort(lista_n, reverse=True)
    pos=list.index(lista_n,media)
    del lista_n[pos:]
    list.sort(lista_n)
    
    return lista_n