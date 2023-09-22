def retira_pontuacao(x):
    '''a função recebe uma frase e retorna a frase onde todos os caracteres de pontuação tenham sido substituidos por espaço
    assinatura: str -> str
    casos de teste:
    '''
	pontos = [',', '!', '.', '?', '-', ':', ';']
    
    for e in pontos:
        x = x.replace(e, ' ')
    return x