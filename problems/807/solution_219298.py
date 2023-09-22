def conta_frases(frase):

    a= str.count(frase, "!",0)
    b = str.count(frase, ".",0)
    c= str.count(frase,"?",0)
    d = str.count(frase, "...",-2)

    return a+b+c+d