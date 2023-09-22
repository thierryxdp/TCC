def inverte (string):
    """Retorna frase invertida str -> str"""
    lista = str.split(retira_pontuacao(string)," ")
    list.reverse (lista)
    return str.join(" ", lista )