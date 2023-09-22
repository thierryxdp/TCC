def retira_pontuacao(x):
    '''a função recebe uma frase e retorna a frase onde todos os caracteres de pontuação tenham sido substituidos por espaço
    assinatura: str -> str
    casos de teste:
    '''
    ls = [',', '!', '.', '?', '-', ':', ';']

    for m in ls:
        x = x.replace(m, ' ')
    return x


def inverte(x):
    """Recebe uma frase e a retorna uma outra frase que contem as mesmas palavras da frase inicial na ordem inversa, sem letras maiusculas e sem pontuacao.
    assinatura: str -> str"""
    x = retira_pontuacao(x)
    x = str.lower(x)
    x = str.split(x)
    x = x[::-1]
    x = str.join(' ', x)
    return x