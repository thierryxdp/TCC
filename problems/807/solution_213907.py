def conta_frases(frase):
    """ Conta o número de frases com base nos pontos que terminam cada frase.
entrada: str
saída: str
"""
    a=frase.replace("..."," ").replace("!"," ").replace("?"," ").replace("."," ")
    frase=a.split()
    return len(frase)