def maiores(lista_numero,n):
    'Dada uma lista com números inteiro, retorna uma lista com todos os números maiores que n. Entradas: list[inteiros], int. Saídas: list[inteiros].'
    lista_numero=sorted(lista_numero+[n])
    resultado=lista_numero[(list.index(lista_numero,n)+1):]
    return resultado