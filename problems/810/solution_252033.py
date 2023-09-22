def retira_pontuacao (frase):
    '''Função que dada uma frase, substitui todos os caracteres de 
    pontuação por espaço
    string -> string'''
    
    pontuacao = ['.', ',', '-', '?', '!', ';']
    list_frase = list(frase)
    
    for pontuacao in pontuacao:
        for pos,char in enumerate(frase):
          if char == pontuacao:
            list_frase[pos] = ' '
    frase = ''.join(list_frase)
    
    return frase

def inverte (frase):
    '''Função que dada uma frase retorna outra frase que contenha as mesmas palavras da frase
    de entrada em ordem inversa, sem letras maiúsculas e sem pontuação
    string -> string'''