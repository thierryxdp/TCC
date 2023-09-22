def maiores(lista,n):
        m=list()
        for h in lista:
            if h>=n:
            m.append(h)
            list.sort(m)
        return m