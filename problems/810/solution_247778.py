#questao de inversão abaixo dessa:
def retira_pontuacao(frase0):
    '''função que dada uma frase retira toda a sua pontuação;
    str->str'''
    if ',' in frase0:
        frase0 = str.replace(frase0,',',' ')
    if '.' in frase0:
        frase0 = str.replace(frase0,'.',' ')
    if ';' in frase0:
        frase0 = str.replace(frase0,';',' ')
    if ':' in frase0:
        frase0 = str.replace(frase0,':',' ')
    if '!' in frase0:
        frase0 = str.replace(frase0,'!',' ')
    if '?' in frase0:
        frase0 = str.replace(frase0,'?',' ')
    if '-' in frase0:
        frase0 = str.replace(frase0,'-',' ')
    if '...' in frase0:
        frase0 = str.replace(frase0,'...',' ')
    return frase0

def inverte (frase0):
    '''função que dado uma frase inverte a ordem de suas palavras deixando
    todas minusculas e sem pontuação; str->str'''
    frase0 = retira_pontuacao(frase0)
    frase0 = (str.lower(frase0)))
    
    return frase0