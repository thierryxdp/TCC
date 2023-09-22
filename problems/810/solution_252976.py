def retira_pontuacao(x):
    '''a função recebe uma frase e retorna a frase onde todos os caracteres de pontuação tenham sido substituidos por espaço
    assinatura: str -> str
    casos de teste:
    retira_pontuacao('oi.') == 'oi'
    retira_pontuacao('caramba! voce por aqui.') == 'caramba coce por aqui'
    '''
    pontos = [',', '!', '.', '?', '-', ':', ';']

    for e in pontos:
        x = x.replace(e, ' ')
    return x


def inverte(x):
    ''' a função recebe uma frase e retorna uma outra frase que contem as mesmas palavras da frase inicial na ordem inversa, sem letras maiusculas e sem pontuacao.
    assinatura: str -> str
    casos de teste:
    inverte('Ainda gosto de chocolate') == 'chocolate de gosto ainda'
    inverte('Caramba eu Adorei') == 'adorei eu caramba'
    '''
    x = retira_pontuacao(x)
    x = str.lower(x)
    x = str.split(x)
    x = x[::-1]
    x = str.join(' ', x)
    return x