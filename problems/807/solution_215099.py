def conta_frases(texto):
    a = texto.split("!")
    b = texto.split("?")
    c = texto.split(".")
    d = texto.split("...")
    i = 0
    for x in range(len(c)):
        if c[x]!= "":
            i = i + 1
            if len(c)> 1:
                if c[x+1]== "":
                    i = i - 1

    print(len(a)-1,len(b)-1,c,i,len(d)-1)