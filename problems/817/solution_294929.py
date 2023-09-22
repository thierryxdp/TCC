def acima_da_media(lista):
    """Funcao que dada uma lista com as notas dos alunos de uma turma, retorne uma lista ordenada com as notas que ficaram acima da média.
    list -> list"""
    
    media = sum(lista)/len(lista)
    
    indice = list.index(lista, media)
    fatiada = [indice+1:]
    
    return fatiada