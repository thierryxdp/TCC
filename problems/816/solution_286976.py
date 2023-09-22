def maiores(numeros: List[int], n: int):
    """Função que dada uma lista de número inteiros e um número inteiro n,
    retorna outra, que contem todos os números da lista original maiores que n,
    odernados em ordem crescente
    list -> list"""
    for i in numeros:
        if i >= n:
            return list(i)
        elif i < n:
            return []