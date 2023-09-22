def lingua_p(palavra):
    vogais = ["a", "e", "i", "o","u"]
    resposta = palavra.lower()
    for i in range(len(palavra)):
        if resposta[i] in vogais:
            resposta_certa = resposta[:i] + "p" + resposta[i:] 
    return resposta_certa