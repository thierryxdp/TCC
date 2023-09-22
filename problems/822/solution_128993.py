def repetidos (lista_n):
    """função que dada uma lista de números, retorna o número de vezes que um elemento da lista é igual ao anterior
    list -> int"""
     cont = 0
    j = 1
    while j < len(lista_n):
        if lista_n[j] == (lista_n[j-1]):
            lista_n.count(lista_n[j])
            cont += 1
        j += 1
    return cont