def acima_da_media(lista):
    """Dada uma lista com as notas dos alunos de uma turma, retorna uma lista ordenada com as notas que ficaram acima da media"""
    
    n=len(lista)
    s=sum(lista)
    media=s//n
    if media in lista:
        m=list.index(lista,media)
        list.sort(lista)
        return lista[m:]
    else:
        list.append(lista,media)
        list.sort(lista)
        mn=list.index(lista,media)
        return lista[mn+1:]