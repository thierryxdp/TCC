def conta_frases(frase):
    final1 = frase.count('.')
    if final1 > 1:
    	final1 = 1
    final2 = frase.count('!')
    final3 = frase.count('?')
    final4 = frase.count('.'+'.'+'.')
    resultado = final1+final2+final3+final4
    return resultado