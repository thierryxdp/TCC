def posLetra(string,letra,posicao):
    ''''''
    if str.count(string,letra) < posicao:
        return -1
    else:
        return str.find(string,letra,posicao)