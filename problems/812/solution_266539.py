def retira_pontuacao(texto):
    """Função que substituir "-", ",", ".", ";", ":" por " "(espaço); str->str"""
    str.replace(texto,'-',' ')
    str.replace(texto,',',' ')
    str.replace(texto,';',' ')
    str.replace(texto,'.',' ')
    str.replace(texto,':',' ')