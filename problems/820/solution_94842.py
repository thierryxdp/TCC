def posLetra(string,letra,numero):
    '''' '''
    quantas = string.count(letra)
    while numero <= quantas or numero > quantas:
        if numero == 1:
            resp = string.find(letra)
            return resp
        elif numero == quantas:
            resp = string.find(letra,quantas)
            return string.find(letra,resp+1)
        elif numero > 1 and numero <= quantas:
            if string.find(letra) == string.find(letra,numero):
                resp = string.find(letra,string.find(letra)+2)
                return resp
            else:
                resp = string.find(letra,quantas+numero+9)
                return resp
        elif numero > quantas:
            resp = -1
            return resp