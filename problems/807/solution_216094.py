# Retorna o número de frases em um texto, sendo
# cada frase podendo ser terminada por
# um ponto, exclamação, ponto de interrogação e reticências
# string -> int
def conta_frases(frase):
    count = frase.count('...')
    frase = frase.replace('...','')
    count += frase.count('.') + frase.count('!') + frase.count('?')
    return count