def conta_frases(texto):
    """Recebe um texto e retorna o número de frases que ele contém"""

    texto = texto.replace("...",'.')

    numPF = str.count(texto,'.')
    numPE = str.count(texto,'!')
    numPI = str.count(texto,'?')


    return numPF + numPE + numPI