def lingua_p(palavra):
    resposta = ''
    for x in palavra:
        if str.upper(x) in "AEIOUÃÕÁÉÍÓÚÂÊÎÔÛ":
            resposta = resposta + "p"+x+"p"
        else:
            resposta = resposta + x
    return resposta