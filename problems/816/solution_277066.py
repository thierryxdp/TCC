def maiores(notas, n):
    list.extend(notas, [n])
    notas.sort()
    del notas[0:n]
    return notas