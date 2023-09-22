def conta_frases(texto):

    a= texto.count(".")
    b=texto.count("!")
    c=texto.count("?")
    d=texto.count("...")
    if "..." in texto:
      return a+b+c+d - (a*3)
    return a+b+c+d