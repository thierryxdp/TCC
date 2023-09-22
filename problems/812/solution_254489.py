def retira_pontuacao(texto):
    '''Retorna o texto sem os caracteres de pontuacao
    str -> str'''
    troca=str.replace
    return troca(texto,'.',' ') and troca(texto,'?',' ') and troca(texto,'!',' ') and troca(texto,'-',' ') and troca(texto,',',' ') and troca(texto,';',' ') and troca(texto,':',' ')