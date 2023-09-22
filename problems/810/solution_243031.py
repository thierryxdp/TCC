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
    list.reverse(fraseb)
    return fraseb