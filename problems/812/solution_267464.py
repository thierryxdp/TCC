def retira_pontuacao(texto):
    """
    """
    string = texto
    new_string = ''.join(filter(str.isalnum, string)) 
    return new_string