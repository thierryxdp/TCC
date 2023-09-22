def faltante(n):
    m = 1
    n2 = n[:]
    while m<len(n2):
        if n2[m] != m + 1:
            n2.insert(m , m)
            m = m + 1
        else:
            m = m + 1
            

    m2 = m + 1
    n2.insert(m2,m2)

    return n2