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

def x(k):
    k = str.split(k,' ')
    return k
def inverte(k):
    k = list.reverse(k)
    return k