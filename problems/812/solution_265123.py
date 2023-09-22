def retira_pontuacao(frase):
    '''
       Dada uma frase a função retorna a frase dada sem os
       caracteres de pontuação presentes na frase
       str -> str
    '''
    str.replace(frase, '.' and '!' and '?' and ',' and '...' and ':' and ';' and '-', ' ')
    return frase