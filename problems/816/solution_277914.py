def maiores(numeros,n):
    list.append(numeros,n)
    list.sort(numeros)
    pos_n=list.index(numeros,n)
    del numeros[0:pos_n]
    return numeros