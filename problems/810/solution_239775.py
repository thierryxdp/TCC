def inverte(texto):
    '''função que, dada uma frase, retorna o inverso dela mesma. str->str'''
    texto = retira_pontuacao(texto)
    texto = str.split(texto)
    texto = texto[: :-1]
    texto = str.join(' ',texto)
    return texto