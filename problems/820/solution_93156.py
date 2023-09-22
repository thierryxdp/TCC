def posLetra(string,letra,numero):
    i=1
    if str.count(string,letra) < numero:
        return -1
    while letra in string:
        if string.count(letra)==1:
            return str.index(string,letra)
        else:
            str.replace(string,letra,i)
            i+=1