def retira_pontuacao(frase):
    ''''''
    return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'-',' '),',',' '),':',' '),';',' '),'.',' '),'!',' '),'?',' ')

def inverte(frase):
    ''''''
    return (str.lower(retira_pontuacao(frase))[-1:]