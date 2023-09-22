def retira_pontuacao(texto):
    """ Retira a pontuação de um texto e retorna-o com espaços no lugar delas"""
    var1 = str.replace(',',' ',texto)
    var2 = str.replace('.',' ',var1)
    var3 = str.replace('?',' ',var2)
    var4 = str.replace('!',' ',var3)
    var5 = str.replace('-',' ',var4)
    var6 = str.replace('...',' ',var5)
    var7 = str.replace(':',' ',var6)
    var8 = str.replace(';',' ',var7)
    return var8