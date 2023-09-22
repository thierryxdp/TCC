def retira_pontuacao(texto):
    '''Dada uma frase, retorna a frase onde todos os caracteres de pontuacao sao substituidos por espaço.;
    string -> string'''
    return texto.replace('.', ' ').replace(',', ' ').replace('!', ' ').replace('?', ' ').replace(';', ' ').replace(':', ' ').replace('-', ' ')

def inverte(frase):
    '''Dada uma frase, retorna outra frase contendo as mesma palavras
    da frase de entrada na ordem inversa;
    string -> string.'''
    return str.join(' ', str.split((retira_pontuacao(frase.lower())))[::-1])