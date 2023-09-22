def retira_pontuacao (frase):
    """ retira as pontuações especiais e coloca espaço."""
    frase = frase.lower()
    frase = str.replace(frase, '!', ' ')
    frase = str.replace(frase, '?', ' ')
    frase = str.replace(frase, ',', ' ')
    frase = str.replace(frase, ':', ' ')
    frase = str.replace(frase, ';', ' ')
    frase = str.replace(frase, '.', ' ')
    frase = str.replace(frase, '-', ' ')
    return frase

def inverte(a):
    g = a.split(' ')
    list.reverse(g)
    j=' '.join(g)
    return j

print(a_string)

c = inverte(a_string)

print(c)
    return j