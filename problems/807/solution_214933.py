def conta_frases(x):
    ponto = len(x.split("."))
    pontvir = len(x.split(";"))  
    dois_pontos = len(x.split(":"))  
    exclamacao = len(x.split("!"))
    interrogacao = len(x.split("?"))                 
    return ponto + pontvir + dois_pontos + exclamacao + interrogacao