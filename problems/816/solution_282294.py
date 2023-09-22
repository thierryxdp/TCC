def maiores(numeros: list[int], n: int) -> list[int]:
    a = numeros.copy()
    a.append(n)
    a.sort()
    b = a.index(n)
    return a[b:]