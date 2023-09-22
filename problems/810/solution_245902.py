def inverte(frase):
    '''retorna a frase invertida com apenas letras minusculas e sem pontuaçao
    str->str'''
    frase=retira_pontuacao(frase)
    frase=str.lower(frase)
    lista=str.split(frase)
    list.reverse(lista)
    frase=str.join(' ',lista)
    return frase