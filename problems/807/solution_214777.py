def conta_frases(frase):
    ""
    finalespaco = str.count(frases,'. ', 0, -3)
    final = str.count(frase, '.', -1)
    exclamacao = str.count(frase, '!")
    interrogacao = str.count(frase, '?')
    quantidadetotal = finalespaco + final + exclamacao + interrogacao 
    return(quantidadetotal)