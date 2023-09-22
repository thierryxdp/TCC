def conta_frases(texto):
    a = texto.split("!")
    b = texto.split("?")
    c = texto.split(".")
    d = texto.split("...")
    i = 0
    
    for x in range(len(c)):
        
        if c[x] == "" and x < len(c):
            i = i+1
    if i%2!=0:
        i=i-1
        i= i* 1.5

    return (len(a)-1+len(b)-1+len(c)-i-1+len(d)-1)