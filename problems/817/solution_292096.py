def acima_da_media (lista):
    """Função que, dada uma lista com as notas dos alunos de uma turma, retorne uma lista ordenada com as notas que ficaram acima da média
    entrada: list
    saída: list"""
    
    media = (sum(lista)/len(lista))
    
    list.append(lista, media)
    list.sort(lista)
    indice = list.index(lista, media)
    
    if lista[indice+1] == int(media):
    	lista_nova = lista[indice+2:]
    
    if lista[indice+1] != int(media):
        lista_nova = lista[indice+1:]
    
    return lista_nova