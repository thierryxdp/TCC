def conta_frases(texto):
    """Funcao que retorna o numero de frases dado um texto como
    parametro;str->int"""
    n1=texto.count("!",texto[0])
    n2=texto.count(".",texto[0])
    n3=texto.count("?",texto[0])
    n4=texto.count("...",texto[0])
    return n1+n2+n3+n4