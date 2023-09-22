def retira_pontuacao(frase):
    'dada uma frase retorne a frase onde todos os caracteres de pontuação tenham sido substituidos por espaço.str-->str'
    frase= str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'-',' '),',',' '),':',' '),';',' '),'!',' '),'.',' '),'?',' '),'...',' ')
    return frase


def inverte(frase1):
    'dada uma frase retorne esta frase na forma inversa sem letras maiusculas e sem pontuação.str-->str'
    frase1= str.lower(frase1)
    frase1= retira_pontuacao(frase1)
    lista=str.split(frase)
    lista.reverse()
    frase=str.join(' ',lista)
    return frase