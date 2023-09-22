def retira_pontuacao(frase):
    frase = str.replace(frase,'?','.')
    frase = str.replace(frase,',','.')
    frase = str.replace(frase,';','.')
    frase = str.replace(frase,'-','.')
    frase = str.replace(frase,'!','.')
    frase = str.replace(frase,'..','.')
    frase1 = str.split(frase,'.')
    frase2 = str.join(' ',frase1)
    return frase2

def x(frase):
    frase = retira_pontuacao(frase)
    frase = str.split(frase,' ')
    return frase
def inverte(frase):
    frase3 = x(frase)
    frase4 = list.reverse(frase3)
    return frase4