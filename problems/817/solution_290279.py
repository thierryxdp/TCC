def acima_da_media (lista):
    """ A função acima_da_media, dada uma lista com as notas dos alunos de uma turma, retorne uma lista ordenada com as notas que ficaram acima da da média.
        
        Parameters:
            lista = lista com as notas dos alunos de uma turma

        Testes:
            acima_da_media([10,0,1,5,6]) = [5, 6, 10]
            acima_da_media([6,6,6,6,7]) = [7]

        Returns:
            lista ordenada com as notas que ficaram acima da da média.
            list --> list
    """
    media = sum(lista)/len(lista)
    
    if media in lista:
        vezes = list.count(lista,media)
        list.append(lista,media)
        list.sort(lista)
        local = list.index(lista,media)
        resultado = lista[local+vezes+1:]
    else:
        list.append(lista,media)
        list.sort(lista)
        local = list.index(lista,media)
        resultado = lista[local+1:]
    return resultado