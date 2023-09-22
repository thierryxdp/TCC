def posLetra(frase,letra,n):
    i = 0 
    resposta = 0
    while i < len(frase):
        if frase[i]==letra:
            resposta = resposta + 1
        i = i + 1
    return resposta