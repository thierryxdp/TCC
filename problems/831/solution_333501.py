def lingua_p(palavra):
    """ - """

    npalavra = palavra.lower()
    resposta0 = npalavra.split("a")
    
    for i in resposta0:
        resposta1 = i + "a" + "p" + "a"
    resposta1 = resposta1.split("e")

    for i in resposta1:
        resposta2 = i + "e"+ "p" + "e"
    resposta2 = resposta2.split("i")

    for i in resposta2:
        resposta3 = i + "i" + "p" + "i"
    resposta3 = resposta3.split("o")

    for i in resposta3:
        resposta4 = i+ "o" + "p" + "o"
    resposta4 = resposta4.split("u")

    for i in resposta4:
        resposta5 = i+"u"+"p"+"u"

    return resposta5