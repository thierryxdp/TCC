def lingua_p(palavra):
    resposta = palavra.lower()
    for i in range(len(palavra)):
        if resposta[i] in "aeiou":
            resposta_certa = resposta[:i] + "p" + resposta[i+1:] 
    return resposta_certa