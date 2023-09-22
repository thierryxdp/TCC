def faltante(l):
    i = 0
    r = 0
    if l[0] < l[len(l) - 1]:
        while i < len(l) - 1:
            if l[i] == l[i + 1] + 1:
                i = i + 1
                r = 0
            elif i == len(l) - 1:
                r = 0
            else:
                r = l[i] + 1
                i = i + 1
        return print(r,'crescente')
    else:
        while i < len(l) - 1:
            if l[i] - 1 == l[i + 1]:
                i = i + 1
            elif i == len(l) - 1:
                r = l[len(l) - 1] - 1
            else:
                r = l[i] - 1
                i = i + 1
            return print(r,'decrescente')
    print(r)