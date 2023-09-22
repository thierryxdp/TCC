def maiores(numeros,n):
    maior_que = n
    filtrados = [x for x in numeros if x > maior_que]
    return sorted(filtrados)