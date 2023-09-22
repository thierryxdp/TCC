def insere(lista_numero, n):
    """Função que recebe uma lista, em ordem crescente, de números inteiros
    e um número inteiro n e incluí n na posição correta.
    list,int->list.
    """
    lista = lista_numero + n
    return list.sort(lista)