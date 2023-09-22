def maiores(lis,n):
    """Função que dada uma lista de número inteiros e um número inteiro n,
    retorna outra, que contem todos os números da lista original maiores que n,
    odernados em ordem crescente
    list -> list"""
    maiores_numeros = list()
    for c in lis:
        if c >= n:
            maiores_numeros.append(c)
    return maiores_numeros
        elif c < n:
        return []