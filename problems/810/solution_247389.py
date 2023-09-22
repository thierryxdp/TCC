def inverte(frase):
    '''Dada uma frase, retorna outra frase contendo as mesma palavras
    da frase de entrada na ordem inversa;
    string -> string.'''
    return str.join(' ', str.split((retira_pontuacao(texto.lower())))[::-1])