def retira_pontuação(frase):
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,';',' ')
    frase=str.replace(frase,'...',' ')
    return frase

def inverte(frase):
    frase = retira_pontuação(frase)
    frase = str.lower(frase)
    frase = str.split(frase,' ')
    list.reverse(frase)
    frase = str.join(',',frase)
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,'  ',' ')
    return frase