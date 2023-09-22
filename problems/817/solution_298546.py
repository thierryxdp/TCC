def acima_da_media(lista):
    """
    Retorna uma lista ordenada com as notas acima da média
    dada uma lista com as notas de alunos de uma turma;
    list -> list
    """
    media = int(sum(lista)/len(lista))
    
    if media in lista:
    	nova = list.sort(lista)
    	ind = list.index(lista,media)
    	maior = lista[ind+1:]
        return maior
    elif media not in lista:
        lista = lista + [media]
    	nova = list.sort(lista)
    	ind = list.index(lista,media+1)
    	maior = lista[ind-2:]
        return maior