def posLetra(string,letra,numero):
    '''' '''
    quantas = string.count(letra)
    contador = 0
    while numero <= quantas:
        if numero == 1:
            resp = string.find(letra)
            return resp
        elif numero > 1 and numero <= quantas:
            if string.find(letra) == string.find(letra,numero):
                resp = string.find(letra,numero+1)
        elif numero > quantas:
            resp = -1
        elif numero == quantas:
            resp = string.find(letra,numero+1)
    return resp