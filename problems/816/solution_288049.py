def maiores(lista,n):
    var1 = []
    for x in lista:
        if x > n:
            var1.append(x)
        var1.sort(x)
        return lista