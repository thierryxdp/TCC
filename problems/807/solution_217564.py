def conta_frases(texto):
    """ A retira todas as pontuações de uma frase e retorna a mesma sem tais pontuações"""
    frase1=texto.replace( '?','#')
    frase2=frase1.replace('!','#')
    frase3=frase2.replace('.','#')
    frase4=frase3.replace('...','#')
    frase5=frase4.split('#')
    frase=len(frase5)
    return frase