def retira_pontuacao(frase):
    """"""
    str.replace(frase,'/',' ')
    str.replace(str.replace(frase,'/',' '),',',' ')
    str.replace(str.replace(str.replace(frase,'/',' '),',',' '),':',' ')
    str.replace(str.replace(str.replace(str.replace(frase,'/',' '),',',' '),':',' '),';',' ')
    str.replace(str.replace(str.replace(str.replace(str.replace(frase,'/',' '),',',' '),':',' '),';',' '),'.',' ')
    return str.replace(str.replace(str.replace(str.replace(str.replace(frase,'/',' '),',',' '),':',' '),';',' '),'.',' ')