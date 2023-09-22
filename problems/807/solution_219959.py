def conta_frases(frase):
    qtd=0
    frase=frase.replace('...','.')
    qtd=frase.count('.')
    qtd=frase.count('!')
    qtd=frase.count('?')
    qtd=frase.count(',')
    qtd=frase.count('.')
    return qtd