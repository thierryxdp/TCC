def retira_pontuacao(frase):
    ''''''
    return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'-',' '),',',' '),':',' '),';',' '),'.',' '),'!',' '),'?',' ')

def inverte(frase):
    ''''''
    return str.join(list.reverse(str.split(str.lower(retira_pontuacao(frase))))