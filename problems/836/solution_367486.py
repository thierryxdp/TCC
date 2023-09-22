def busca(setor, M):
    """função que retorna uma lista com os dados dos funcionários do setor indicado, se nenhum registro for encontrado, retorna uma lista vazia
    str, list -> list"""
    listadosetor = []
    for i in range(len(M)):
        if setor in M[i]:
            list.remove(M[i],setor)
            list.append(listadosetor, M[i])
    return listadosetor