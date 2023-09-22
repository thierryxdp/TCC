def posLetra(string,letra,numero):
    quantidade = str.count(string,letra)
    return str.find(string,letra,0,quantidade-numero)