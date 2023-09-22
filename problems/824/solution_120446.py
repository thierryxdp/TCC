def teste (frase):
    x=0
    resposta = []
    FRASE = str.upper(frase)
    while x<=len(frase)-1:
        if FRASE[x] in "EAIOU":
            resposta = str.replace(FRASE, FRASE[x], str.lower(FRASE[x]))
        x=x+1
    return str(resposta)