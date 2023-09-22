def retira_pontuacao(texto):
    """ Retira a pontuação de um texto e retorna-o com espaços no lugar delas"""
    str.replace(texto,'.',' ')
    str.replace(texto,'?',' ')
    str.replace(texto,'!',' ')
    str.replace(texto,'...',' ')
    str.replace(texto,'-',' ')
    str.replace(texto,':',' ')
    str.replace(texto,';',' ')
    str.replace(texto,',',' ')