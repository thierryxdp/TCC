def retira_pontuacao(frase):
    ''''''
    return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'-',' '),',',' '),':',' '),';',' '),'.',' '),'!',' '),'?',' ')

def inverte(frase):
    ''''''
    frasefinal=(str.split(str.lower(retira_pontuacao(frase))))
    list.reverse(frasefinal)
    return str.join(frasefinal)