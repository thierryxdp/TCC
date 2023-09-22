def posLetra(string,letra,numero):
    quantidade = str.count(string,letra)
    if numero==1:
        return str.find(string,letra,0)
    else:
        return str.find(string,letra,quantidade-numero)