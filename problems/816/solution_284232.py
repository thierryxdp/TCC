def maiores(lista_numero,n):
    """Função, que dada um lista de números inteiros e um número inteiro n, retorna outra listaque contenha todos os números maiores que n e em ordem crescente."""
    """list,int->list"""
    lista = lista_numero + [n]
    list.sort(lista)
    lista_maior = lista[-1:n]
    return lista_maior