def conta_frases(frases):
    """Função que calcula a quantidade de frases dada de entrada por uma str e ao identificar os separadores retornar a quantidade de frases"
    str -> int """
    Quantidade_frases = frases.replace("?","/").replace("...","/").replace("!","/").replace(".","/")
    
    return len(Quantidade_frases.split("/"))-1