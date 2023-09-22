def retira_pontuacao(frase):
    '''Função que dada uma frase, retorna a frase onde todos os caracteres de pontuação são substituídos por espaço: string -> string'''
    return (re.sub('-|,|:|;|.|?|!|...',' ',frase))