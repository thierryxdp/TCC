def acima_da_media(lista):
    """Dada uma lista com as notas dos alunos de uma turma, retorna uma lista ordenada com as notas que ficaram acima da media"""
    lista.append(m)
    list.sort(lista)
    n=len(lista)
    s=sum(lista)
    media=s//n
    m=list.index(lista,media)
    
    
    return lista[m+1:]