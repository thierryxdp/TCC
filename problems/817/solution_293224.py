def acima_da_media(lista):
    """" faz a média das notas dos alunos e retorna uma lista daqueles que ficaram acima da média;list->list"""
    
    m=sum(lista)
    q=len(lista)
    z= m//q
    list.append(lista,z)
    list.sort(lista)
    x=list.index(lista,z)
    lista2=lista[x:]
    return lista2