def retira_pontuacao(frase):
    frase = str.replace(frase,'?','.')
    frase = str.replace(frase,',','.')
    frase = str.replace(frase,';','.')
    frase = str.replace(frase,'-','.')
    frase = str.replace(frase,'!','.')
    frase = str.replace(frase,'..','.')
    frase1 = str.split(frase,'.')
    return frase1

def inverte(frase):
    fraseb = retira_pontuacao(frase)
    frasec = str.split(fraseb, ' ')
    list.reverse(frasec)
    return fraseb