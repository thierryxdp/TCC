def posLetra(string,letra,numero):
    '''' '''
    quantas = string.count(letra)
    while numero <= quantas or numero > quantas:
        if numero == 1:
            resp = string.find(letra)
            return resp
        elif numero == quantas:
            resp = string.find(letra,quantas)
            return resp
        elif numero > 1 and numero <= quantas:
            if string.find(letra) == string.find(letra,numero):
                resp = string.find(letra,string.find(letra)+2)
                return resp
        elif numero > quantas:
            resp = -1
            return resp