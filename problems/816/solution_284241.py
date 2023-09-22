def maiores(lista, n):
    """Função que dada uma lista de números inteiros e um número inteiro n, retorna outra lista;
    que conetenha todos os números da lista original maiores que n, em ordem crescente;
    list, int -> list"""
    return [i for i in lista if i>n]