def retira_pontuacao(x):
    '''a função recebe uma frase e retorna a frase onde todos os caracteres de pontuação tenham sido substituidos por espaço
    assinatura: str -> str
    casos de teste:
    '''
    pontos = [',', '!', '.', '?', '-', ':', ';']

    for e in pontos:
        x = x.replace(e, ' ')
    return x

def inverte(x):
    '''a funcao recebe uma frase e retorna a mesma frase com a ordem das palavras invertidas, sem letra maiuscula e sem pontuacao
    assinatura: str -> str
    '''
    return str.lower(x) and reversed(x)