def conta_frases(frase):
    if '...' in frase:
        if frase[len(frase)]=='.':
  	      return 1+ frase.count('...')+frase.count('?')+frase.count('!')+frase.count('. ')
  		else:
            return frase.count('...')+frase.count('?')+frase.count('!')+frase.count('. ')

    else:
        return frase.count('.')+frase.count('!')+frase.count('?')