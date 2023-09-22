def posLetra(string,letra,numero):
    inicio = 0
    c = []
    if numero>(str.count(string,letra)):
        return -1
    while inicio < len(string):
        resultado = string.find(letra, inicio)
        if resultado == -1: 
            break
        c.append(resultado)
        inicio = resultado + 1   
    return c[numero-1]