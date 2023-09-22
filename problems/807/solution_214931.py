def conta_frases(x):
    ponto = len(x.split(".")
    ponto_virgula = len(x.split(";")  
    dois_pontos = len(x.split(":")  
    exclamacao = len(x.split("!")
    interrogacao = len(x.split("?")                 
    return ponto + ponto_virgula + dois_pontos + exclamacao + interrogacao