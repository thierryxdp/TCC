def retira_pontuacao(texto):
    ''' Essa função troca todos os caracteres de pontuação por espaço.'''
    ''' Entrada = string ; saída = string '''
    if '.' in texto:
        novo_texto = str.replace(texto,'.',' ')
        return novo_texto
    elif ',' in texto:
        novo_texto = str.replace(texto,',',' ')
        return novo_texto