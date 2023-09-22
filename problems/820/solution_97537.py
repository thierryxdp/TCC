def posLetra(frase,letra,n):
    i = 0
    inicio = 0
    resposta = 0
    while i<n:
        inicio = str.find(frase,letra,inicio) + 1
        resposta = inicio -1
        i = i + 1
    return resposta