def inverte(frase):
'''Reverte as palavras de uma frase.'''
palavras = frase.split()
palavras.reverse()
return ' '.join(palavras)