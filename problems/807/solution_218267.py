def conta_frases(texto):
    """Funcao que retorna o numero de frases dado um texto como
    parametro;str->int"""
    n1=texto.count("!")
    n2=texto.count(". ")
    n3=texto.count("?")
    n4=texto.count("...")
    return n1+n2+n3+n4