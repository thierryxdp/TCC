def retira_pontuacao(frase):
    """
    Códoigo que retorna uma determinada string substituindo
    pontuação por espaço.
    :entrada --> string:
    :return --> string
    """
    z2='-',',',':',';','.'
    frase1= frase.replace('.', ' ')
    frase2= frase1.replace(',', ' ')
    frase3= frase2.replace('-', ' ')
    frase4= frase3.replace(':',' ')
    frase5= frase4.replace(';', ' ')
    frase6= frase5.replace('?', ' ')
    frase7= frase5.replace('!', ' ')
    return frase7