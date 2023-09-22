def retira_pontuacao(string):
    '''Função que recebe uma string e retorna ela sem nenhum caracter de pontuação.
    Esses caracteres serão substituídos por espaço. str->str'''
    subs_exclamacao=string.replace('!',' ')
    subs_reticencias=subs_exclamacao.replace('...',' ')
    subs_interrogacao=subs_reticencias.replace('?',' ')
    subs_pontovirgula=subs_interrogacao.replace(';',' ')
    subs_travessao=subs_pontovirgula.replace('-',' ')
    subs_2pontos=subs_travessao.replace(':',' ')
    subs_virgula=subs_2pontos.replace(',',' ')
    string_pronta=subs_virgula.replace('.',' ')
    return string_pronta