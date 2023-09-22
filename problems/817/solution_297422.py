def acima_da_media (lista):
    """dada uma lista com as notas dos alunos de uma turma, retorne uma lista ordenada com as notas que ficaram acima da média.
    
    entrada->lista
    retorna->lista"""
    list.sort (lista)
    somanotas=sum (lista)
    alunos= len (lista)
    media=somanotas/alunos
    
    if lista [0]> media:
        return lista
    elif lista [1]>media and len (lista)>1:
        return lista [1:]
    elif lista [2]>media and len (lista)>2:
        return lista [2:]