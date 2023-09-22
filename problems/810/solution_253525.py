def retira_pontuacao(frase):
    caracteres = '-,:;.!?'
    for c in caracteres:
        frase = frase.replace(c, ' ')
    return frase
def inverte(frase):
    a = frase.split()
    b = a[::-1]
    c = ' '.join(b)
    d = c.lower()
    return d