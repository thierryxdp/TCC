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