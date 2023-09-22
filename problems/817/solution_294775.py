def acima_da_media(lista):
    '''dada uma lista com as notas dos alunos de uma turma, retorna
    uma lista ordenada com as notas que ficaram acima da media
    lista -> lista'''
    media = sum(lista)/len(lista)
    
    list.sort(lista)
    indice= list.index(lista,media)
    fatiada=[media 1:]
    
    return fatiada