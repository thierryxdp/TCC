def repetidos(numeros: List[int], n: int):
    for i in numeros:
        if i > n:
            return list(i)