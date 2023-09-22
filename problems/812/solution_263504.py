def retira_pontuacao(texto):
    '''Dada uma frase, retorna a frase onde todos os caracteres de pontuacao sao substituidos por espaço.;
    string -> string'''
    return texto.replace('.', ' ').replace(',', ' ').replace('!', ' ').replace('?', ' ').replace(';', ' ').replace(':', ' ').replace('-', ' ')