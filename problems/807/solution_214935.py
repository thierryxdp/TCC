def conta_frases(x):
    if len(x.split(".")) >=0:
    	ponto = len(x.split("."))
    if len(x.split(";")) >=0:
    	ponto_virgula = len(x.split(";")) 
    if len(x.split(":"))>=0:
    	dois_pontos = len(x.split(":"))  
    if len(x.split("!")) >=0:
    	exclamacao = len(x.split("!"))
    if len(x.split("?"))>=0:
    	interrogacao = len(x.split("?"))                 
    return ponto + ponto_virgula + dois_pontos + exclamacao + interrogacao