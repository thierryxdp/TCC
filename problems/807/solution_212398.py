def conta_frases(frase):
    soma= frase.count('! ') + frase.count('. ') + frase.count('? ') + frase.count('... ')
   	if '!' or '?' or '.' or '...':
        soma+=1
    return soma