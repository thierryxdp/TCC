def lingua_p(palavra):
    resposta = palavra.lower()
    for i in range(len(palavra)):
        if resposta[i] in "aeiou":
            resposta = resposta[:i] + "p" + resposta[i+2:] 
    return resposta