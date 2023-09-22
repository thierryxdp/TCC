def posLetra(string,letra,numero):
    ''' '''
    ocorrencia = 0
    while numero < len(string):
        if numero == 1:
            ans = string.find(letra)
            return ans
        elif numero != 0:
            ans = string.find(letra,frase.find(letra,2)+1)
            return ans
        ocorrencia += 1
    return ans