def intercala(lista1, lista2):
    """função que recebe duas listas de tamanho 3 e que retorna uma nova
    lista, que concatena as duas listas de entrada e intercala seus elementos;
    tupla->tupla"""
    lista_int = [lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],lista2[2]]
    if lista1%3==0 and lista2%3==0:
        return lista_int
    else:
        return ''