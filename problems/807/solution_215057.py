def conta_frases(texto):
    """ funçao que conta o numero de frases em um texto. str -> int"""
    texto1= str.count(texto, "...")
    frase= str.replace(texto, '...',' ')
    texto1= texto1+str.count(frase,'!')
    texto1=texto1+str.count(frase,'?')
    texto1= texto1+str.count(frase,'.')
    return texto1