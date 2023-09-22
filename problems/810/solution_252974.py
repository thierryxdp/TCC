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
    ''' a função recebe uma frase e retorna uma outra frase que contem as mesmas palavras da frase inicial na ordem inversa, sem letras maiusculas e sem pontuacao.
    assinatura: str -> str
    casos de teste:
    '''
    x = retira_pontuacao(x)
    x = str.lower(x)
    x = str.split(x)
    x = x[::-1]
    x = str.join('', x)
    return x