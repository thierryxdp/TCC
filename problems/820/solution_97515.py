def posLetra(frase,letra,n):
    i = 0
    resposta = 0
    while i<n:
        resposta = str.find(frase,letra,i)
        i = i + 1
    return resposta