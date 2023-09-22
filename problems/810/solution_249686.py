def inverte(frase):
    '''retorna  a frase invertida, sem letras maiúsculas e se pontução. str -> str'''
    list_frase = str.split(retira_pontuacao(frase))
    list.reverse (list_frase)
    return str.lower(str.join(' ', list_frase))