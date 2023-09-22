def retira_pontuacao(text):
    """Recebe um texto e retorna ele modificado com separadores apenas como espacos
    str --> str"""

    text = str.replace(text,'...',' ')
    text = str.replace(text,'.',' ')
    text = str.replace(text,'!',' ')
    text = str.replace(text,'?',' ')
    text = str.replace(text,'-',' ')
    text = str.replace(text,',',' ')
    text = str.replace(text,':',' ')
    text = str.replace(text,';',' ')

    return text