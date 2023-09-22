def retira_pontuacao(frase):
    '''
    dada uma frase, retorna ela mesma mas com sua
    pontuação substituída por espaços
    
    string -> string
    '''
    
    frase.replace(',', ' ')
    frase.replace('-', ' ')
    frase.replace('.', ' ')
    frase.replace(',', ' ')
    frase.replace(';', ' ')
    frase.replace('!', ' ')
    frase.replace('?', ' ')
    frase.replace(':', ' ')
    return frase