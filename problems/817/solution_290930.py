def acima_da_media(lista):
    """Dada uma lista com as notas de um aluno, retorna-se uma lista com as
    notas que ficaram acima da media obtida entre elas
    Entrada: lista
    Return: lista"""
    list.sort(lista)
    media = sum(lista)/len(lista)
    lista2 = lista + [media]
    list.sort(lista2)
    i = list.index(lista2,media)
    return lista2[(i+1):]