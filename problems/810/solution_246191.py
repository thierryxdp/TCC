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
    '''função que dada uma frase retorna outra frase que contém 
    as mesmas palavras so que em ordem inversa. str -> str'''
    texto = retira_pontuacao(texto)
    texto = str.lower(texto)
    texto = str.split(texto)
    texto = texto[: :-1]
    texto = str.join(' ',texto)
    return texto