def inverte (string):
    '''funcao que inverte as strings e retira as pontuacoes'''
    lista = str.split(retira_pontuacao(string)," ")
    list.reverse (lista)
    return str.join(" ", lista )