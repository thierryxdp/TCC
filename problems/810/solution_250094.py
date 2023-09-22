def retira_pontuacao(frase):
    return str.replace(str.replace(str.replacr(str.replace(str.replace(str.replace(str.replace(frase,',',' '),'.',' '),':',' '),';',' '),'!',' '),'?',' '),'-',' ')

def inverte(frase1):
    lista = str.split(retira_pontuacao(frase1))
    list.reverse(lista)
    return str.join(' ',lista)