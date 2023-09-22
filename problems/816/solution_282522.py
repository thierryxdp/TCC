def maiores(lista, numero):
    """Função que recebe uma lista, um número que é
    inserido na lista e retorna uma lista com todos
    os números maiores que o número inserido
    list, int -> list"""
    list.append(lista,numero)
    list.sort(lista)
    return lista[list.index(lista,numero)+1:]