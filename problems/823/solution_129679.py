def faltante(peçasT,peças):
    n = 0
    list.sort(peçasT)
    list.sort(peças)
    while peçasT[n] == peças[n]:
        n = n + 1
    return n +1