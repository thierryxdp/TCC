def retira_pontuacao(texto):
    ''' Essa função troca todos os caracteres de pontuação por espaço.'''
    ''' Entrada = string ; saída = string '''
    i = 0
    novo_texto = ''
    lista = [',','.',';',':','-','.']
    while i < len(lista):
        if lista[i] in texto:
            novo_texto = novo_texto + str.replace(texto,lista[i],' ')
        i = i + 1
    return novo_texto