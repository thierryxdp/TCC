def retira_pontuacao(frase):
    frase = str.replace(frase,'-','')
    frase = str.replace(frase,'!','')
    frase = str.replace(frase,'?','')
    frase = str.replace(frase,'.','')
    frase = str.replace(frase,';','')
    frase = str.replace(frase,',','')
    return frase
def inverte(frase):
    frase = retira_pontuacao(frase)
    lista = str.split(frase)
    lista = lista[::-1]
    str.join(lista)