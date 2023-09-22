def posLetra(string,letra,numero):
    x=0
    while x<len(string):
        if letra in string:
            return list(string).index(letra)