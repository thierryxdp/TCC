def retira_pontuacao(string):
    """Substitui caracteres de pontuação como vírgulas, travessão, dois pontos, ponto e vírgula e também ponto final por espaço em branco
    str -> str"""
    
    string = string.replace(',', ' ')
    string = string.replace('-', ' ')
    string = string.replace(':', ' ')
    string = string.replace('.', ' ')
    string = string.replace(';', ' ')
    return  string