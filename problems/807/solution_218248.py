def conta_frases(texto):
    """Funcao que retorna o numero de frases dado um texto como
    parametro;str->int"""
    n1=texto.count("!",texto[0:len(texto)])
    n2=texto.count(".",texto[0:len(texto)])
    n3=texto.count("?",texto[0:len(texto)])
    n4=texto.count("...",texto[0:len(texto)])
    return n1+n2+n3+n4