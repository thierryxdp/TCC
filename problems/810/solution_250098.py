def retira_pontuacao(frase):
    return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,',',' '),'.',' '),':',' '),';',' '),'!',' '),'?',' '),'-',' ')

def inverte(frase1):
    frase2 = retira_pontuacao(frase1)
    lista = str.split(frase2)
    list.reverse(lista)
    return str.join(' ',lista)