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
    
    ordenada = sorted(lista)
    indice = list.index(ordenada,media)
    lista_acima = ordenada[indice+2:]

    return lista_acima