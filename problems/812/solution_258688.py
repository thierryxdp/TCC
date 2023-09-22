def retira_pontuacao(texto):
    """função que retira dado um texto, retira suas pontuações
str -> str"""
    if '.' in texto:
        return str.replace(texto,'.',' ')
    if ',' in texto:
        return str.replace(texto,',',' ')
    if ',' and '.' in texto:
        return str.replace(texto,',' and '.',' ')
    if '!' in texto:
        return str.replace(texto,'!',' ')
    elif '?' in texto:
        return str.replace(texto,'?',' ')
    else:
        return texto