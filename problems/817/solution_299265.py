def acima_da_media (lista):
    """dada como entrada uma lsita com as notas de uam turma, a função
    retorna uma lista ordenada com as notas que ficaram acima da média.
    list -> list"""
    
    media = sum(lista)/len(lista)
    
    novalista = list.append(lista, media)
    list.sort(novalista)
    
    indice = list.index(novalista, media)
    
    return novalista[indice+1:]