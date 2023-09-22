def acima_da_media(lista):
    """" faz a média das notas dos alunos e retorna uma lista daqueles que ficaram acima da média;list->list"""
    
    m=sum(lista)
    q=m/len(lista)
    w= int(q)
    l= list.append(lista,w)
    list.sort(l)
    
    return l[w+1:]