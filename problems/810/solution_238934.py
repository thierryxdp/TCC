def retira_pontuacao(texto):
    texto=str.replace(texto,'-',' ')
    texto=str.replace(texto,',',' ')
    texto=str.replace(texto,':',' ')
    texto=str.replace(texto,';',' ')
    texto=str.replace(texto,'?',' ')
    texto=str.replace(texto,'!',' ')
    texto=str.replace(texto,'...',' ')
    texto=str.replace(texto,'.',' ')
    return texto
def inverte(texto):
    retira_pontuacao(texto)
    str.split(texto)
    texto=texto[::-1]
    return str.join(' ',texto)