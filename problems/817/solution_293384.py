def acima_da_media(lista):
    """" faz a média das notas dos alunos e retorna uma lista daqueles que ficaram acima da média;list->list"""
    
    m=sum(lista)
    q=len(lista)
    z= m//q
    w= q+1
    list.append(lista,w)
    list.sort(lista)
    x=list.index(lista,w)
    lista2=lista[x:]
    return lista2