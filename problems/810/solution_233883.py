def inverte(frase):

    frase = str.replace(frase,".", " ")
    frase = str.replace(frase,",", " ")
    frase = str.replace(frase,":", " ")
    frase = str.replace (frase,"-"," ")
    frase = str.replace(frase,";"," ")
    frase = str.replace(frase,"!"," ")
    frase = str.replace(frase,"?"," ")

    SepararFrase = str.split(frase)
    JuntarFrase = str.join(" ",SepararFrase)

    return JuntarFrase[::-1]