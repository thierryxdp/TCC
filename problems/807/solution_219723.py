def conta_frases(x):
    # str-> int
    #vai dar o numero de pontos da frase
    x2=x+" "
    nint = len(x2.split("?"))-1
    n3p = len(x2.split("..."))-1
    n1p = len(x2.split("."))-1
    nexc = len(x2.split("!"))-1
    return nint+nexc+n3p+n1p-3*n3p