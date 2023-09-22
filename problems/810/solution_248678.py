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
    frase= retira_pontuacao(frase)
    frase= frase.lower()
    lista= frase.split()
    lista.reverse()
    frase= " ".join(str(palavra) for palavra in lista)
    return frase