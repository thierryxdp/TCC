def maiores(num_inteiros,n):
    """funcao que recebe uma lista de notas e retorna uma nova lista com as notas que ficaram acima da media
    list -> list"""
    list.append(num_inteiros,n)
    list.sort(num_inteiros)
    ps=list.index(num_inteiros,n)
    lista=num_inteiros[ps+1:]
    return lista


def acima_da_media(lista):
    media=sum(lista)
    maiores=maiores( lista,media)
    return maiores