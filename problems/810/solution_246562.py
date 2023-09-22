def retira_pontuacao(frase):
    frase_alterada = frase
    frase_alterada = frase_alterada.replace('!',' ')
    frase_alterada = frase_alterada.replace('?',' ')
    frase_alterada = frase_alterada.replace('...',' ')
    frase_alterada = frase_alterada.replace(',',' ')
    frase_alterada = frase_alterada.replace('-',' ')
    frase_alterada = frase_alterada.replace(',',' ')
    frase_alterada = frase_alterada.replace(':',' ')
    frase_alterada = frase_alterada.replace(';',' ')
    frase_alterada = frase_alterada.replace('.',' ')
    return frase_alterada

def inverte(frase):
    f1 = frase
    f1 = retira_pontuacao(frase)
    f1 = str.lower(f1)
    f1 = str.split(f1)
    f1 = str.join(f1,' ')
    return f1