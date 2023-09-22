def acima_da_media(lista):
    """" faz a média das notas dos alunos e retorna uma lista daqueles que ficaram acima da média;list->list"""
    
    m=sum(lista)
    q=list.index(lista)
    z= m//q
    list.append(lista,z)
    list.sort(lista)
    lista2=lista[z+1:]
    return lista2