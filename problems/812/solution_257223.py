def retira_pontuacao(string):
    """Substitui caracteres de pontuação por espaço em branco
    str -> str"""
    
    string = string.replace(',', ' ')
    string = string.replace('-', ' ')
    string = string.replace(':', ' ')
    string = string.replace('.', ' ')
    string = string.replace(';', ' ')
    string = string.replace('!', ' ')
    string = string.replace('?', ' ')
    
    return  string