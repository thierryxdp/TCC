def conta_frases(frase):
"""""""
sem_ret = str.replace(frase, '...', '.')
pFinal = str.count(sem_ret, '.')
pExc = str.count(frase, '!')
pInt = str.count(frase, '?')
total_frases = pFinal + pExc + pInt
return total_frases