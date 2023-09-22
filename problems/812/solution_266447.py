def retira_pontuacao(frase):
    """ Retira todas as pontuações do texto e as substitui por espaçoes"""
    if str.find('.') > 0:
        return str.replace(frase,'.',' ')
    elif str.find(',') > 0:
        return str.replace(frase,',',' ')
    elif str.find(';') > 0:
        return str.replace(frase,';',' ')
    elif str.find(':') > 0:
        return str.replace(frase,':',' ')
    elif str.find('!') > 0:
        return str.replace(frase,'!',' ')
    elif str.find('?') > 0:
        return str.replace(frase,'?',' ')
    elif str.find('-') > 0:
        return str.replace(frase,'-',' ')
    elif str.find('/') > 0:
        return str.replace(frase,'/',' ')