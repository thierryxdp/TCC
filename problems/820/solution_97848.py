def posLetra(string,letra,numero):
    a = letra[:numero]
    b = a.index(a)
    if a in string:
        return b