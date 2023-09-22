def conta_frases (frase):
    '''Conta a quantidade de frases, str->int'''
    x = str.count ('...',frase[0:])
    a = list(frase)
   return a.count ('.') + a.count('!') + a.count('?') - 2 * x