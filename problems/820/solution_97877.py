def posLetra(string,letra,numero):
    a = string.find(letra[:numero])
    if a in string :
        return a
    else:
        return a