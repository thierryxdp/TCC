def contafrase(frase):

    a= str.count(frase, "!")
    b = str.count(frase, ".")
    c= str.count(frase,"?")
    d = str.count(frase, "...")

    return a+b+c+d