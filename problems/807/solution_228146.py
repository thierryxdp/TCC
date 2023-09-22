def conta_frases(texto):
    """Funcao que conta o numero de frases contidos em um texto"""
    frase=texto
    frase=str.replace(frase,"...",".")
    return str.count(frase,".") + str.count(frase,"?") + str.count(frase,"!")