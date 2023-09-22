def conta_frases(texto):
    a = texto.split("!")
    b = texto.split("?")
    c = texto.split(".")
    d = texto.split("...")
    i = 0
    print(a,b,c,d)
    print(len(c))
    for x in range(len(c)):
        print("inicio",x)
        if c[x] == "" and x < len(c):
            print("entrei")
            print(c[x])
            i = i+1
            print("final",x)
    if i%2!=0:
        i=i-1
        i= i* 1.5

    return (len(a)-1+len(b)-1+len(c)-i-1+len(d)-1)