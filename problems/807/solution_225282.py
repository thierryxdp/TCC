def conta_frases(frase)
"""conta as frases
str>int"""
return frase.count('.')+frase.count('!')+frase.count('?')-2*frase.count('...')