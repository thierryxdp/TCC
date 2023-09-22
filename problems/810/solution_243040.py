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

def inverte(frase):
    frase1 = str.split(frase,' ')
    list.reverse(frase1)
    return frase1