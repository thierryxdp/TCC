def acima_da_media(lista):
    """Dá uma lista ordenada com alunos que ficaram acima da média
    	list -> list
        Parameters:
        lista: Lista com notas dos alunos
        
        Returns:
        Lista ordenada com alunos que ficaram acima da média
     """
    media = sum(lista)/len(lista)
    list.append(lista,media)
    list.sort(lista)
    p = list.index(lista,media)
    n = list.count(lista,media)
    
    return lista[p+1:]