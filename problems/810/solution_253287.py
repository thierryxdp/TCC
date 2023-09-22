def inverte(frase):
    for x in '!?.:;-,':
        frase=frase.replace(x,' ')
    frase1=str.split(frase)
    list.reverse(frase1)
    frase_final=str.join(',',frase1)
    return str.lower(frase_final.replace(x,' '))