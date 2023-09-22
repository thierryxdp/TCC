def maiores(numeros,n):
    maior_que = n
    filtrados = [x for x in notas if x > maior_que]
    return sorted(filtrados)