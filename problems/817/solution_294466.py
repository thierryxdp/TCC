def acima_da_media(lista):
    """Essa função recebe uma lista com as notas da turma
    e retorna apenas aquelas acima da média. list->list"""
    media = sum(lista)//len(lista)
    lista2 = [elem for elem in lista if elem > media]
    lista2.sort(reverse = False)
    return lista2