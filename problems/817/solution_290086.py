def acima_da_media(lista_notas:list) -> list:
    """Dada a lista de notas de uma turma, mostra apenas as notas acima
       da média da turma
       
       Parameters:
       lista_notas: lista de notas da turma
       
       Returns:
       lista com as notas maiores que a média
    """
    media = sum(lista_notas) / len(lista_notas)
    
    list.append(lista_notas, media)
    list.sort(lista_notas)
    indice = list.index(lista_notas, media)
    list.remove(lista_notas, media)
    
    return lista_notas[indice +1:]