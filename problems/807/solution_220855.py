def conta_frases(frase):
     "Conta a quantidade de frases em um texto"
        frase=frase.replace('...','.')
        return frase.count('.')+frase.count('!')+frase.count('?')+1