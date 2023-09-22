def maiores(lista,n):
    """ Retorna os números da lista original que são maiores que o número de entrada"""
    list.append(lista,n)
    list.sort(lista)
    indice = list.index(lista,n)
    return lista[indice+1:]

def acima_da_media(lista):
    """Essa função retorna uma lista com as notas acima da media, em ordem, do aluno."""
    media = sum(lista)/len(lista)   
    lista_final = maiores(lista,media)
    return lista_final