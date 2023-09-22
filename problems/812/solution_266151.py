def retira_pontuacao(texto):
    """ Retira a pontuação de um texto e retorna-o com espaços no lugar delas"""
    var1 = [',','.','?','!','-',';',':','...']
    return str.replace(var1, ' ', texto)