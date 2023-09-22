def retira_pontuacao(frase):
    """"jhjhhi """"
    if '/' in frase:
        return str.replace(frase,'/',' ')
    x = str.replace(frase,',',' ')
    y = str.replace(frase,':',' ')
    w = str.replace(frase,';',' ')
    z = str.replace(frase,'.',' ')
    a = str.replace(frase,'!',' ')