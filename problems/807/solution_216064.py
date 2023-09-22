'''Substitui todo tipo de pontuação por '.' e conta a quantidade de frases, diminuindo o ponto final'''
def conta_frases(frase):
    frase = frase.replace('...','.').replace('!','.').replace('?','.')
    frase = frase.split('.')
    return len(frase)-1