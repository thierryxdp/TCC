def retira_pontuacao(x):
    '''Esta função substitui todos os caracteres de pontuação, incluindo
travess̃ao, v́ırgula, dois pontos, ponto e v́ırgula, além da pontuaç̃ao de encerramento de frase, por um espaço.
str->str'''
    if '!' in x:
        x=str.replace(x,'!',' ')
    if '?' in x:
        x=str.replace(x,'?',' ')
    if '.' in x:
        x=str.replace(x,'.',' ')
    if '...' in x:
        x=str.replace(x,'...',' ')
    if ':' in x:
        x=str.replace(x,':',' ')
    if ';' in x:
        x=str.replace(x,';',' ')
    if ',' in x:
        x=str.replace(x,',',' ')
    if '-' in x:
        x=str.replace(x,'-',' ')
        
    return x