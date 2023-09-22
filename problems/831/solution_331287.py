def lingua_p(palavra):
    resposta = palavra.lower()
    vogais = "aeiou"
    for i in range(len(palavra)):
        if resposta[i] in vogais:
            resposta = resposta[i] + "p" + resposta[i+1,]
    return resposta