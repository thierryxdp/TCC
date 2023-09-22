def conta_frases(frase):
    """ Conta o número de frases com base nos pontos que terminam cada frase.
entrada: str
saída: str
"""
    frase=frase.replace("."," ").replace("!"," ").replace("?"," ").replace("..."," ")
    frase=frase.split
    frase=str.count(frase)
    return frase