#Mirella Maturo da Cruz DRE:119023985 Questão 4 do Laboratório 5
def retira_pontuacao(frase):
    '''Retorna uma frase onde todos os caracteres de pontuação são
    substituidos por espaço'''
    
    frase = frase.replace('!', ' ')
    frase = frase.replace ('...', ' ')
    frase = frase.replace ('.', ' ')
    frase = frase.replace ('?', ' ')
    frase = frase.replace ('_', ' ')
    frase = frase.replace (':', ' ')
    frase = frase.replace ('-', ' ')
    frase = frase.replace (',', ' ')
    return frase