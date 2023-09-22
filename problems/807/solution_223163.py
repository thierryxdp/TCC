def conta_frases(msg):
    """ funcao que dada um texto como parametro de entrada, ira retornar a quantidade de frases contida na mensagem.
str -> int """


    ppasso = str.replace(msg, "!", ".") 
    spasso = str.replace(ppasso, "?", ".")
    retisensia = '...'
    tpasso = str.replace(spasso, retisensia, ".")
    qpasso = str.split(tpasso,'.')

    return len(qpasso)-1