def retira_pontuacao(frase):   
    if ('.' in frase):
        frase = frase.replace('.', ' ')
    if ('-' in frase):
        frase = frase.replace('-', ' ')
    if (',' in frase):
        frase = frase.replace(',',' ')
    if (':' in frase):
        frase = frase.replace(':', ' ')
    if (';' in frase):
        frase = frase.replace(';', ' ')
    if ('?' in frase):
        frase = frase.replace('?', ' ')
    if ('!' in frase):
        frase = frase.replace('!', ' ')
    return frase

def inverte(frase):
    frase = retira_pontuacao(frase)
    frase = frase.lower()
    frase = frase.split()
    frase.reverse()
    x = ""
    for i in frase:
        x += i + " "
    return x[:-1]