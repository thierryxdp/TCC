# Retira a pontuação
# periodo
# str->str
def retira_pontuacao(periodo):
    """Função que dada a str de entrada substitui a potuação por espaços"""
    """str->str"""
    potuacao= "." and ";" and "!" and "?" and "..." and "-" and ":"
    return str.replace(periodo,potuacao," ")