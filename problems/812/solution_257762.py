def retira_pontuacao(frase):
    '''dada uma frase retorna ela mesma com todos os caracteres de pontuação substituidos por espaço
    retorna: str -> str'''
    
    frase = frase.replace('—', ' ')
    frase = frase.replace(';', ' ')
    frase = frase.replace('.', ' ')
    frase = frase.replace(',', ' ')
    frase = frase.replace('!', ' ')
    frase = frase.replace('?', ' ')
    frase = frase.replace('...', ' ')
    frase = frase.replace('-', ' ')
    
    return frase