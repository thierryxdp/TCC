def retira_pontuacao(frase):
    '''função que receba uma frase e retorne a mesma frase, mas sem a pontuação original.
    str->str'''
    frase= str.replace (frase,'...',' ')
    frase= str.replace (frase,'.',' ')
    frase= str.replace (frase,'!',' ')
    frase= str.replace (frase,'?',' ')
    frase= str.replace (frase,':',' ')
    frase= str.replace (frase,'-',' ')
    frase= str.replace (frase,',',' ')
    frase= str.replace (frase,';',' ')
    return frase

def inverte(frase):
    frase= str.split(frase)
    return frase