def acima_da_media(lista):
    """" faz a média das notas dos alunos e retorna uma lista daqueles que ficaram acima da média;list->list"""
    
    m=sum(lista)
    q=len(lista)
    z=m//q
    list.extend(lista,[z])
    list.sort(lista)
    w=list.index(lista,z)
    lista1=lista[w:]
    list.remove(lista1,z)
    return lista1