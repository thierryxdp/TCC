def acima_da_media(lista):
    """" faz a média das notas dos alunos e retorna uma lista daqueles que ficaram acima da média;list->list"""
    
    m=sum(lista)
    q=m//len(lista)
    w= int(q)
    list.append(lista,w)
    list.sort(lista)
    z=list.index(w,0)
    lista2=lista[z:]
    return lista2