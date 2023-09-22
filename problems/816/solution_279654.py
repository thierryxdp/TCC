# Questão 4
def maiores(lista_numero, n):
    """Função que dada uma lista de números inteiros, retorna outra lista com
    os números maiores que 'n';
    list, int -> list"""
    list.append(lista_numero, n)
    list.sort(lista_numero)
    indice = list.index(lista_numero, n)
    return lista_numero[indice + 1 :]