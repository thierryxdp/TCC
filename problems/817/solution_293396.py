def acima_da_media(lista):
    """" faz a média das notas dos alunos e retorna uma lista daqueles que ficaram acima da média;list->list"""
    
    m=sum(lista)
    q=len(lista)
    z=m//q
    list.extend(lista,[z])
    list.sort(lista)
    w=list.index(lista,z)
    lista1=lista[w:]
    if list.count(lista1,z)==2:
        return lista[w+2:]
    else:
        if list.count(lista1,z)<2:
            return lista[w+1:]