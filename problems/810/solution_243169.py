def retira_pontuacao(frase):
    '''recebe uma frase e retorna a mesma frase retirando 
   		a pontuação e substituindo por espaço
        str->str'''
    if '.' in frase:
        frase = str.replace(frase,'.',' ')
    if '-' in frase:
        frase = str.replace(frase,'-',' ')
    if ',' in frase:
        frase = str.replace(frase,',',' ')
    if ':' in frase:
        frase = str.replace(frase,':',' ')
    if ';' in frase:
        frase = str.replace(frase,';',' ')
    if '!' in frase:
        frase = str.replace(frase,'!',' ')
    if '?' in frase:
        frase = str.replace(frase,'?',' ')
    return frase

def inverte(frase):
    '''recebe uma frase e a retorna de forma inversa,
    sem pontuação e sem letra maiúscula
    str->str'''
    frase = str.lower(retira_pontuacao(frase))
    out = list.reverse(str.split(frase))
    return out