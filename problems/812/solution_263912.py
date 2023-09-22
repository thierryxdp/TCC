def retira_pontuacao(frase):
    '''Dada uma frase, retorna a frase onde todos os 
    caracteres de pontuação, substituidos por espaço
    string -> string'''
    lista = []
    lista += [frase]
    if '/' or '!' or ',' or ':' or ';' in lista:
        frase.replace('/', ' ')
        frase.replace(',', ' ')
        frase.replace(':', ' ')
        frase.replace(';', ' ')
        frase.replace('!', ' ')
        return frase