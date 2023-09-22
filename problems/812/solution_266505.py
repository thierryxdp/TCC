def retira_pontuacao (frase):
    '''Função que dada uma frase, retorna a frase onde todos
    os caracteres de pontuação são substituídos por espaço
    string -> string'''
    
    pontuacao = [',', '-', ':', ';', '!', '?', '.']
    
    for c in pontuacao:
        frase = frase.replace(c, ' ')