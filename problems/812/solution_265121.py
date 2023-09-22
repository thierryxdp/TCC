def retira_pontuacao(frase):
    '''
       Dada uma frase a função retorna a frase dada sem os
       caracteres de pontuação presentes na frase
       str -> str
    '''
    frase = str.split(frase,'.' and '!' and '?' and ',' and ':' and ';' and ',' and '...' and '-')
    frase = str.join(' ', frase)
    return frase