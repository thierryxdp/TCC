def acima_da_media(lista):
    """essa funçao recebe uma lista com notas de alunos e retorna, em ordem crescente, aquelas acima da media"""
    """entrada: list"""
    """saida: list"""
    list.sort(lista)
    m=(sum(lista)/len(lista))
    lista[lista.index(m):lista.index(m)]=[m]
    return lista[((lista.index(m))+1:]