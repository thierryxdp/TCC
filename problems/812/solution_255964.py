def retira_pontuacao(frase):
    """"""
    return str.replace(frase,'/',' ')
    return str.replace(str.replace(frase,'/',' '),',',' ')
    return str.replace(str.replace(str.replace(frase,'/',' '),',',' '),':',' ')
    return str.replace(str.replace(str.replace(str.replace(frase,'/',' '),',',' '),':',' '),';',' ')
    return str.replace(str.replace(str.replace(str.replace(str.replace(frase,'/',' '),',',' '),':',' '),';',' '),'.',' ')