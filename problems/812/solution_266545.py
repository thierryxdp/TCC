def retira_pontuacao(x):
    '''a função recebe uma frase e retorna a frase onde todos os caracteres de pontuação tenham sido substituidos por espaço
    assinatura: str -> str
    casos de teste:
    '''

    x1 = str.replace(x, '.',' ')
    x2 = str.replace(x, '?',' ')
    x3 = str.replace(x, '!',' ')
    x4 = str.replace(x, '-',' ') 
    x5 = str.replace(x, ',',' ') 
    x6 = str.replace(x, ':',' ') 
    x7 = str.replace(x, ';',' ')

    return x1 + x2 + x3 + x4 + x5 + x6 + x7