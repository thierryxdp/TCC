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
    
    if x1 or x2 or x3 or x4 or x5 or x6 or x7 in x:
        return str.replace(x, ',' , ' ')