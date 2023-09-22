def lingua_p(palavra):
    '''Funcao recebe uma string em portugues e a traduz para a lingua p. Tal traducao e feita da sehuinte forma. Apos toda vogal, e adcionado um pp seguido da mesma vogal passada
string -> string'''
    nova_frase = ''
    alteracao = ''
    for i in str.lower(palavra):
        if (i in 'aeiouáéíóúàèìòù'):
            alteracao = i + 'p' + i
        else:
            alteracao = i
        nova_frase += alteracao
    return nova_frase