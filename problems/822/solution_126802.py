def repetidos(L):
    contador = 0
    resposta = 0
    while contador < len(L):
        if L[contador] == L[contador - 1]:
            resposta = resposta +  1
            contador = contador + 1
        elif L[contador] != L[contador -1]:
            contador = contador + 1
    return resposta