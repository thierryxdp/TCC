def retira_pontuacao(frase):
    'dado um texto, remove as pontuações'
    frase=str.replace(frase,'...',' ')
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    frase=str.replace(frase,'?',' ')
    return frase
def inverte(frase):
    frase_sep=str.split(frase)
    frase_inv=frase_sep[::-1]
    return str.join(' ',frase_inv)