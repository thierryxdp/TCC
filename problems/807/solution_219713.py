def conta_frases(x):
    # str-> int
    #vai dar o numero de pontos da frase
    return len(x.split("."))+len(x.split("!"))+len(x.split("?"))