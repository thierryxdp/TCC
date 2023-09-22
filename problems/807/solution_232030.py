def conta_frases(texto):
    """Conta as frases que o texto de entrada tem, fazendo a subistituição de toda pontiaçãp por #;str==>int"""
    texto1=texto.replace("...","#")
    texto2=texto1.replace(".","#")
    texto3=texto2.replace("!","#")
    texto4=texto3.replace("?","#")    
    return texto4.count("#")