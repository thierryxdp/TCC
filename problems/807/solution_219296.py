def conta_frase(frase):

    a= str.count(frase, "!")
    b = str.count(frase, ".")
    c= str.count(frase,"?")
    d = str.count(frase, "...")

    return a+b+c+(-2)*d