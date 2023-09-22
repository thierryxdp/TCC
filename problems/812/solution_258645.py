def retira_pontuacao(frase):
    '''Função que dada uma frase, retorna uma frase onde todos os caracteres de pontuação (incluindo travessão, vírgula, dois pontos, ponto e vírgula, além da pontuação
    de encerramento de frase) tenham sido substituídos por espaço
    str -> str'''
    
    return str.strip(frase, '-,:;.!?')