def retira_pontuacao (frase):
    '''Função que dada uma frase, substitui todos os caracteres de 
    pontuação por espaço
    string -> string'''
    
    pontuacao = ['.', ',', '-', '?', '!', ';']
    list_frase = list(texto)
    
    for pontuacao in pontuacoes:
        for pos,char in enumerate(texto):
            if char == pontuacao
            list_frase[pos] = ' '
    frase = ''.join(list_frase)
    return frase