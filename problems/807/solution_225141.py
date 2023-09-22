def conta_frases(frase):
''' '''
sem_ret = str.replace(frase, '...', '.')
return str.count(sem_ret, '.') + str.count(frase, '!') + str.count(frase, '?')