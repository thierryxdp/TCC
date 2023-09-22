def maiores(numeros: List[int], n: int):
    """funçao que recebe uma lista de numeros e um numero inteiro e retorna outra lista contendo os numeros da lista original maiores que n
    lista, int -> lista"""
    return sorted([i for i in numeros if i > n])