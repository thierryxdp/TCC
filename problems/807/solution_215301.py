def conta_frases(texto):
     '''Conta o número de frases em um texto;
     str -> int'''
     frases = texto.replace('...','.')
     frase1 = frases.count('!')
     frase2 = frases.count ('.')
     frase3 = frases.count ('?')
     
     return frase1 + frase2 + frase3