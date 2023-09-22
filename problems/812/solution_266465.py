def retira_pontuacao(frase):
    """ Retira todas as pontuações do texto e as substitui por espaçoes"""
    if str.index(frase,'.',[0,]) > 0:
        return str.replace(frase,'.',' ')
    elif str.find(frase,',',[0,]) > 0:
        return str.replace(frase,',',' ')
    elif str.find(frase,';',[0,]) > 0:
        return str.replace(frase,';',' ')
    elif str.find(frase,':',[0,]) > 0:
        return str.replace(frase,':',' ')
    elif str.find(frase,'!',[0,]) > 0:
        return str.replace(frase,'!',' ')
    elif str.find(frase,'?',[0,]) > 0:
        return str.replace(frase,'?',' ')
    elif str.find(frase,'-',[0,]) > 0:
        return str.replace(frase,'-',' ')
    elif str.find(frase,'/',[0,]) > 0:
        return str.replace(frase,'/',' ')