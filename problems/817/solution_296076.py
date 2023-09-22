def acima_da_media(lista):
    """essa funçao recebe uma lista com notas de alunos e retorna, em ordem crescente, aquelas acima da media"""
    """entrada: list"""
    """saida: list"""
    m=(sum(lista)/len(lista))
    list.append(lista,m)
    list.sort(lista)
    return lista