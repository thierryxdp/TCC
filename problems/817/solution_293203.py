def acima_da_media(lista):
    """" faz a média das notas dos alunos e retorna uma lista daqueles que ficaram acima da média;list->list"""
    
    m=sum(lista)
    q=m//len(lista)
    list.append(lista,q)
    list.sort(lista)
    lista2=lista[q+1:]
    return lista2