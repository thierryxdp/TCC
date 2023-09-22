def filtra_pares(quatro_elementos):
    '''Função que recebe quatro elementos inteiros em uma
    tupla, verificas quais desses são pares e os retorna
    em uma nova tupla
    (int, int, int, int) -> (tuple)'''
    lista_temporaria = []
    for n in quatro_elementos:
        if n%2 == 0:
            lista_temporaria.append(n)
    tupla_final = tuple(lista_temporaria)
    return tupla_final