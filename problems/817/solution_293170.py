def acima_da_media(lista):
    """" faz a média das notas dos alunos e retorna uma lista daqueles que ficaram acima da média;list->list"""
    list.sort(lista)
    m=sum(lista)
    q=m/len(lista)
    w= int(q)
    return lista[len(w)+1:]