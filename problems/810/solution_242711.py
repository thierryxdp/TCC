def inverte (frase):
    '''funçao que substituí pontuações na frase de entrada por espaço, retornando a frase s pontuações'''
    '''str->str'''
    texto=str.replace(frase,"."," ")
    texto=str.replace(texto,","," ")
    texto=str.replace(texto,"!"," ")
    texto=str.replace(texto,"?"," ")
    texto=str.replace(texto,"-"," ")
    str.lower(texto)
    novafrase=str.split(texto)
    list.reverse(novafrase)
    return novafrase