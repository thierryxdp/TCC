def inverte(frase):
    '''Essa fução retorna uma frase na ordem inversa, em letras minnúsculas e sem pontuação,
    str->str'''
    for x in '.:;-,?!':
        frase=frase.replace(x,' ')
    frase1=str.split(frase)
    list.reverse(frase1)
    frase_final=str.join(',',frase1)
    return str.lower(frase_final.replace(x,' '))