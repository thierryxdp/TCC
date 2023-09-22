def retira_pontuacao(texto):
    ''' Essa função troca todos os caracteres de pontuação por espaço.'''
    ''' Entrada = string ; saída = string '''
    lista = [',','.',';',':','-','.']
    if lista in texto:
        return str.replace(texto,lista[i],' ')