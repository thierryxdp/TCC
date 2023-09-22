def retira_pontuacao(x):
    '''a função recebe uma frase e retorna a frase onde todos os caracteres de pontuação tenham sido substituidos por espaço
    assinatura: str -> str
    casos de teste:
    '''
    pontuacao = ['.', '?', '!', '-', ',', ':', ';']
    
    if pontuacao in x:
        returnstr.replace(x, pontuacao, ' ')