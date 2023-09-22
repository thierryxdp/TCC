def retira_pontuacao(texto):
    """
    """
    string = texto
    new_string = ''.split(filter(str.isalnum, string)) 
    return new_string