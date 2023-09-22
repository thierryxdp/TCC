def filtraMultiplos(lista_num, n):
    """Função que recebe uma lista e filtra os multiplos de um certo numero n e retorna uma  com elementos da lista original que forem
divisiveis por este numero n"""
    lista_multiplos = []
    indice = 0
    n = int(n)
    while indice < len(lista_num):
        if lista_num[indice]%n == 0:
            lista_multiplos = lista_multiplos + [lista_num[indice],]
        indice = indice + 1
    return lista_multiplos