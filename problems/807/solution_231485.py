def conta_frases(frase):
    final1 = frase.count('.')
    final2 = frase.count('!')
    final3 = frase.count('?')
    final4 = frase.count('.'+'.'+'.')
    if final4 > 3:
    	final4 = 0
    resultado = final1+final2+final3+final4
    return resultado