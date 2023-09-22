def conta_frases (frase):
    '''Conta a quantidade de frases, str->int'''
    d = str.split(frase) 
    x = d.count ("aula...") + d.count("tarde...") + d.count ('estimação...') + d.count ("dacolá...")
    frase = list(frase)
    return frase.count ('.') + frase.count('!') + frase.count('?') - (2 * x)