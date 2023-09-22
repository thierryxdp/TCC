#Questão 5 -------------------------------------------------------

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
    lista = str.split(frase)
    juntos= str.join(' ',lista) 
    inverte = (juntos[-1:0])
    pontuacao = retira_pontuacao(inverte)
    minusculas= str.lower(pontuacao)
    return minusculas