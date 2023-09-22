def posLetra(string,letra,numero):
    quantidade = str.count(string,letra)
    return str.find(string,letra,quantidade-1-numero)