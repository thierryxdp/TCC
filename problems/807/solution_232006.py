def conta_frases(texto):
    """função que conta frases num texto. entrada string e saída int"""
    contadorDeFrases = 0
    qntDeReticencias = (len(texto.split('...')) - 1)
    if (qntDeReticencias > 0):
        contadorDeFrases -= qntDeReticencias * 3
    contadorDeFrases += (len(texto.split('.')) - 1)
    contadorDeFrases += (len(texto.split('?')) - 1)
    contadorDeFrases += (len(texto.split('!')) - 1)
    contadorDeFrases += qntDeReticencias
    return contadorDeFrases