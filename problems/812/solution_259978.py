def retira_pontuacao(frase):
    '''Recebe uma frase e a retorna com os caracteres de pontuacao sendo substituido por espaços
    string -> string'''
    frase=frase.replace('-','')
    frase=frase.replace(',','')
    frase=frase.replace(':','')
    frase=frase.replace(';','')
    frase=frase.replace('!','')
    frase=frase.replace('?','')
    frase=frase.replace('.','')
    frase=frase.replace('...','')
    return frase