def retirapontuacao(frase):
    """retira a pontuação de uma dada frase"""
    frase = frase.replace(',',' ')
    return frase
def inverte(frase):
    frase = retirapontuacao(frase)
    frase = frase.split()
    return frase