def maiores (numeros: List[int], n: int):
    'Funcaoo que retorna os numeros maiores que n em ordem crescente'
    for i in numeros:
        if i > n:
            return list(i)