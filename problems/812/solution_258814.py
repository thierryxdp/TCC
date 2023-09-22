def retira_pontuacao(frase):
    """ """
    if '.' in frase :
        return str.replace(str.replace(frase,'.',' '),'!',' ')
    else:
        frase