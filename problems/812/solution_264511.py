def retira_pontuacao(frase):
    '''funcao que dada uma frase retorne uma frase onde todos os caracteres de pontuação sjam substituidos por espaço
    str->str'''
    str.join(frase," ")
    if "." in frase:
        return str.replace(frase,'.',' ')
    if "," in frase:
        return str.replace(frase,',',' ')
    if "!" in frase:
        return str.replace(frase,'!',' ')
    if "?" in frase:
        return str.replace(frase,'?',' ')