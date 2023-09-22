def maiores(lista, n):
    """Retorna todos os números de uma lista maiores que n.
    Entrada: list, float
    Saída: list
    """
    list.append(lista, n)
    list.sort(lista)
    o = list.index(lista, n)+1
    return lista[o:]

def acima_da_media(lista):
    """Retorna uma lista com as notas da turma que ficaram acima da média, em ordem.
    Entrada: list
    Saída: list
    """
    media = sum(lista) / len(lista)
    if media in lista:
        B = maiores(lista, media)
    	list.remove (B, media)
    	return B
    else:
        return B