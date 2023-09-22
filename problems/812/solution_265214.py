def retira_pontuacao(texto):
    ''' Essa função troca todos os caracteres de pontuação por espaço.'''
    ''' Entrada = string ; saída = string '''
    if '.' in texto:
        novo_texto = str.replace(texto,'.',' ')
        return novo_texto
    elif ',' and '-' and '.' in texto:
        novo_texto = str.replace(texto,','and'-'and'.',' ')
        return novo_texto