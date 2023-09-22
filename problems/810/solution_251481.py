def retira_pontuacao(frase):
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    return frase

def inverte(frase):
    frase=frase
    frase=str.lower(frase)
    frase=retira_pontuacao(frase)
    frase=str.split(frase)
    frase=str.join(list.reverse(frase))
    return frase