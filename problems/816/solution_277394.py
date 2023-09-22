def maiores(numeros: List[int], n: int):
    lista1 = (3,4,6)
    for i in numeros:
        if i > n:
            return list(i)