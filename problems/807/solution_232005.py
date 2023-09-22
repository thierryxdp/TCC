def conta_frases(texto):
    """função que conta frases num texto. entrada string e saída int"""
    contadorDeFrases = 0
    contadorDeFrases += (len(texto.split('.')) - 1)
    contadorDeFrases += (len(texto.split('?')) - 1)
    contadorDeFrases += (len(texto.split('!')) - 1)
    contadorDeFrases += (len(texto.split('...')) - 1)
    return contadorDeFrases