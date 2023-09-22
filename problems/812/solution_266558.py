def retira_pontuacao(x):
    '''a função recebe uma frase e retorna a frase onde todos os caracteres de pontuação tenham sido substituidos por espaço
    assinatura: str -> str
    casos de teste:
    '''

    x1 = str.replace(x, /./g,' ')
    x2 = str.replace(x, /?/g,' ')
    x3 = str.replace(x, /!/g,' ')
    x4 = str.replace(x, /-/g,' ') 
    x5 = str.replace(x, /,/g,' ') 
    x6 = str.replace(x, /:/g,' ') 
    x7 = str.replace(x, /;/g,' ')

    return x1 andx2 and x3 and x4 and x5 and x6 and x7