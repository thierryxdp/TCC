def posLetra(string,letra,numero):
    if str.count(string,letra) < numero:
        return -1
    return str.index(string,letra,numero)