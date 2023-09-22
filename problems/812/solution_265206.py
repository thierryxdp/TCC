def retira_pontuacao(texto):
    ''' Essa função troca todos os caracteres de pontuação por espaço.'''
    ''' Entrada = string ; saída = string '''
    letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    i = 0
    nova_letra = ''
    while i < len(letras):
        if texto[i]!= letras:
            nova_letra = nova_letra + str.replace(texto,texto[i],' ')
        i = i + 1
    return nova_letra