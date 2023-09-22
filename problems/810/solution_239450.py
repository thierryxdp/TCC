def retira_pontuacao(frase):
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,'...',' ')
    frase=str.replace(frase,'.',' ')
    return frase

def inverte(frase):
    '''Função que retorna o inverso de uma frase dada
    frase=str->str'''
    frase = str.split(retira_pontuacao(frase),' ')
    frase = str.join(retira_pontuacao(frase),' ')
    frase = str.lower(retira_pontuacao(frase),' ')
    frase = [-1:]
    return frase