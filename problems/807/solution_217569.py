def conta_frases(texto):
    """ A retira todas as pontuações de uma frase e retorna a mesma sem tais pontuações"""
    frase1=texto.replace( '?' and '!','.')
    frase2=frase1.replace('.','.')
    frase3=frase2.replace('...','.')
    frase4=frase3.split('.')
    frase=len(frase4)
    return frase