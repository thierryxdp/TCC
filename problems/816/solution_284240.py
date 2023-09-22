def maiores(lista, n):
    """Função que dada uma lista de números inteiros e um número inteiro n, retorna outra lista;
    que conetenha todos os números da lista original maiores que n, em ordem crescente;
    list, int -> list"""
    nmaiores = list()
    for c in lista:
        if c>= n:
            nmaiores.append(c)
            return nmaiores