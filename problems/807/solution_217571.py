def conta_frases(texto):
    """ A retira todas as pontuações de uma frase e retorna a mesma sem tais pontuações"""
    frase1=texto.replace( '?' and '!','.')
    frase2=frase1.replace('...'and'.','.')
    frase3=frase2.split('.')
    frase=len(frase3)
    return frase