def maiores(lista,n):
    if n not in lista:
        list.append(lista,n)
    list.sort(lista)
    ind=list.index(lista,n)
    listaf=lista[ind+1:]
    return listaf

def acima_da_media(lista):
    """ essa funcao calcula uma lista com as notas dos alunos de uma turma, e retorna uma lista ordenada com as notas que ficaram acima da media; list -> list"""
    media=sum(lista)/len(lista)
    return maiores(lista,media)