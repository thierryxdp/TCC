def retira_pontuacao(x):
    '''a função recebe uma frase e retorna a frase onde todos os caracteres de pontuação tenham sido substituidos por espaço
    assinatura: str -> str
    casos de teste:
    '''
	x1 = '.'
    x2 = '?'
    x3 = '!'
    x4 = '-'
    x5 = ','
    x6 = ':'
    x7 = ';'
    
    if x1 or x2 or x3 or x4 or x5 or x6 or x7 in x:
        return srt.replace(x, x1 , ' ')