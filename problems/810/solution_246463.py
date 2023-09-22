def inverte(frase):
    """funçao que dada uma frase retorna a frase com as
    palavras na ordem inversa; str->str"""
    frase1=str.replace(frase, '-', ' ')
    frase2=str.replace(frase1, ',', '')
    frase3=str.replace(frase2, ':', '')
    frase4=str.replace(frase3, ';', '')
    frase5=str.replace(frase4, '...', '')
    frase6=str.replace(frase5, '?', '')
    frase7=str.replace(frase6, '!', '')
    frase8=str.replace(frase7, '.', '')
    frase9=str.lower(frase8)
    frase10=frase9.split(' ')
    frase11=frase10[::-1]
    return str.join(' ', frase11)