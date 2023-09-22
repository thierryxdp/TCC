def retira_pontuacao(texto):
    """função que retira dado um texto, retira suas pontuações
str -> str"""
    texto = str.replace(texto,'!',' ')
    texto = str.replace(texto,'?',' ')
    texto = str.replace(texto,'.',' ')
    texto = str.replace(texto,',',' ')
    texto = str.replace(texto,'-',' ')
    return texto
def inverte(texto):
    texto = retira_pontuacao(texto)
    texto = str.split(texto)
    texto = texto[: :-1]
    texto = str.join(' ',texto)
    return texto