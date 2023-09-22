def retirapontuacao(s):
    """retira a pontuação de uma dada frase"""
    frase = frase.replace('!','')
    frase = frase.replace(',','')
    frase = frase.replace(';','')
    frase = frase.replace('.','')
    return s