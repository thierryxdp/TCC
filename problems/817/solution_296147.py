def maiores(lista,m):
    if m in lista:
        list.sort(lista)
        return lista[list.count(lista,m)+list.index(lista,m):]
    elif m not in lista:
        list.append(lista,m)
        list.sort(lista)
        return lista[list.index(lista,m)+1:]
    
def acima_da_media(lista):
    """dada uma lista com as notas dos alunos,
    retorna uma lista ordena com a s notas
    que ficaram acima da média;
    list[int]->list[int]"""
    m=sum(lista)/len(lista)
    return maiores(lista,m)