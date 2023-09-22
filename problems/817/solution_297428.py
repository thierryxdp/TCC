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
    elif lista [1]>media and len (lista)>0:
        return lista [1:]
    elif lista [2]>media and len (lista)>2:
        return lista [2:]
    elif lista [3]>media and len(lista)>3:
        return lista[3:]
    elif lista [4]>media and len(lista)>4:
        return lista [4:]
    elif lista[5]>media and len(lista)>5:
        return lista [5:]
    elif lista [6]>media and len(lista)>6:
        return lista [6:]
    elif lista [7]>media and len(lista)>7:
        return lista [7]
    else:
        return []