def conta_frases(frase):
    x = str.split(frase,'...' )
    y = str.split(frase,'?') 

    return len(x + y)