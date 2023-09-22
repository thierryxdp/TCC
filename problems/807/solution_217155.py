def conta_frases(frase):
    x = str.split(frase,'.' )
    y = str.split(frase,'!') 
    z = str.split(frase,'?') 
    y = str.split(frase,'...') 

    f = x+y+z+y

    return len(f )