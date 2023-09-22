def conta_frases(texto):
    '''funcao conta a quantidade de frases no texto. str->int'''
    a=texto.count("?")
    b=texto.count("!")
    c=texto.count(".")
    d=texto.count("...")
    return a+b+c-2*d