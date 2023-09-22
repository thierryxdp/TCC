def maiores(lista, n):    
    if n not in lista:
        list.append(lista, n)
        
    list.sort(lista)
    indice = list.index(lista, n)
    
    lista2 = lista[indice+1:]
    return lista2

def acima_da_media(lista):
    
    """Dada uma lista com as notas dos alunos, retorna
    as que ficaram acima da média. list -> list  """
    media = sum(lista)/len(lista)
    return media