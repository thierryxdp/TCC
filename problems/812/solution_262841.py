def retira_pontuacao(texto):
    """função que retira dado um texto, retira suas pontuações
str -> str"""
    texto = str.replace(texto,'!',' ')
    texto = str.replace(texto,'?',' ')
    texto = str.replace(texto,'.',' ')
    texto = str.replace(texto,',',' ')
    texto = str.replace(texto,'-',' ')
    return texto