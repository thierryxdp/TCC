def retira_pontuacao(frase):
    frase= frase.replace(',',' ')
    frase= frase.replace('/',' ')
    frase= frase.replace(';',' ')
    frase= frase.replace(':',' ')
    frase= frase.replace('.',' ')
    frase= frase.replace('?',' ')
    frase= frase.replace('!',' ')
    frase= frase.replace('-',' ')
    return frase
def inverte(frase):
    frase= frase.lower()
    lista= frase.split(" ")
    lista= lista.reverse()
    return lista