def retira_pontuacao(frase, pontuacao='- , : ; .'):
    '''Retorna uma frase com os caracteres de pontuação 
    substituídospor espaços
    string -> string '''
    
    for x in pontuacao:
        texto = texto.replace(x, ' ')
    return texto