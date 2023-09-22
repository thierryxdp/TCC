def acima_da_media(lista):
    """" faz a média das notas dos alunos e retorna uma lista daqueles que ficaram acima da média;list->list"""
    
    m=sum(lista)
    q=len(lista)
    z= m//q
    list.append(lista,z)
    list.sort(lista)
    x=list.index(lista,z)
    lista1=lista[x+2:]
    lista2=lista[x+1:]
    if z==4:
        return lista2
    else:
        if z!=4:
            return lista1