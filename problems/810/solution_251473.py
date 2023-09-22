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
    frase=retira_pontucao(frase)
    frase=str.split(frase)
    return frase