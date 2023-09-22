def retira_pontuacao (frase):
    '''Função que dada uma frase, substitui todos os caracteres de 
    pontuação por espaço
    string -> string'''
    
    pontuacao = ['.', ',', '-', '?', '!', ';']
    list_frase = list(frase)
    
    for pontuacao in pontuacoes:
        for pos,char in enumerate(frase):
          if char == pontuacao:
            list_frase[pos] = ' '
    frase = ''.join(list_frase)
    return frase