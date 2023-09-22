def conta_frases(frase):
    if '...' in frase:
        if frase[len(frase)-1]=='.' and not(frase[len(frase)-2]=='.'):
            return 1+ frase.count('...')+frase.count('?')+frase.count('!')+frase.count('. ')
		else:
            return frase.count('...')+frase.count('?')+frase.count('!')+frase.count('. ')

    else:
        return frase.count('.')+frase.count('!')+frase.count('?')