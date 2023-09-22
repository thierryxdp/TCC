def posLetra(string,letra,numero):
    ''' '''
    ocorrencia = 0
    while numero < len(string):
        if numero == 1:
            ans = string.find(letra)
            return ans
        elif numero != 0:
            ans = string.find(letra,numero - ocorrencia)
            return ans
        ocorrencia += 1
    ans = -1
    return ans