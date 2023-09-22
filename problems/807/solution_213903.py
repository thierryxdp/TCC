def conta_frases(frase):
    """ Conta o número de frases com base nos pontos que terminam cada frase.
entrada: str
saída: str
"""
    frase=frase.split(frase.replace("..."," ").replace("!"," ").replace("?"," ").replace("."," "))
    return frase