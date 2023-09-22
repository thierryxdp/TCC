def acima_da_media(lista):
    """Funcao que dada uma lista com as notas dos alunos de uma turma, retorne uma lista ordenada com as notas que ficaram acima da media.
    list -> list"""
    
    media = sum(lista)/len(lista)
    
    list.sort(lista)
    ind = list.index(lista,media)
    fatiada = [media+1:]
    
    return fatiada