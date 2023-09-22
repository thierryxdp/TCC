def inverte(texto):
    '''função que, dada uma frase, retira as pontuações nela existentes e
retorna o inverso dela mesma. str->str'''
    texto = str.capitalize(texto)
    texto = str.replace(texto,'!',' ')
    texto = str.replace(texto,'?',' ')
    texto = str.replace(texto,'.',' ')
    texto = str.replace(texto,',',' ')
    texto = str.replace(texto,'-',' ')
    texto = str.split(texto)
    texto = texto[: :-1]
    texto = str.join(' ',texto)
    return texto