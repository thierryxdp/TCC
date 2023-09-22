def retira_pontuacao(x):
    '''função recebe uma frase de entrada e retorna a frase sem a pontuação.
    string -> string'''
    if ',' in x:
        x.replace(',', '')
    if '.' in x:
        x.replace('.', '')
    if '!' in x:
        x.replace('!', '')
    if '?' in x: 
        x.replace('?', '')
    if '-' in x:
        x.replace('-', '')
    if ';' in x:
        x.replace(';', '')
    if ':' in x: 
        x.replace(':', '')
    return x