def conta_frases(frase):
    return len(frase.split('.')) or len(frase.split('?')) or len(frase.split('!'))