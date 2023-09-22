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
    texto=str.lower(texto)
    texto=retira_pontuacao(texto)
    texto=str.split(texto)
    texto=texto[::-1]
    return str.join(' ',texto)