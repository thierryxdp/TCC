def retira_pontuacao(frase):
    '''Dada uma frase, retorna a frase onde todos os 
    caracteres de pontuação, substituidos por espaço
    string -> string'''
    lista = []
    lista += [frase]
    if '/'or ',' or ':' or ';' in frase:
        frase.replace('/', ' ')
        frase.replace(',', ' ')
        frase.replace(':', ' ')
        frase.replace(';', ' ')
        return frase