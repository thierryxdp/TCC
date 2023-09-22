def retira_pontuacao(frase):
    return str.replace(str.replace(str.replacr(str.replace(str.replace(str.replace(str.replace(frase,',',' '),'.',' '),':',' '),';',' '),'!',' '),'?',' '),'-',' ')

def inverte(frase1):
    return retira_pontuacao(list.reverse(str.split(frase1)))