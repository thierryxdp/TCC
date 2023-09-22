def qtd_divisores(n):
    faclist = [1]
    for i in range(2, int(m.sqrt(n) + 2)):
        if n%i == 0:
            if i not in faclist:
                faclist.append(i)
                if n/i not in faclist:
                    faclist.append(n/i)
    return facts