def substitui(frase):
    '''
        dada uma frase, substitui todo os caracteres de pontuação por ' '
        str -> str
    '''
    text1=str.replace(frase,'.',' ')
    text2=str.replace(text1,'!',' ')
    text3=str.replace(text2,'?',' ')
    text4=str.replace(text3,',',' ')
    text5=str.replace(text4,'-',' ')
    text6=str.replace(text5,':',' ')
    text7=str.replace(text6,';',' ')
    text8=str.replace(text7,'...',' ')
    return text8

def inverte(texto):
    '''
        dado um texto retira todas as pontuações e retorna o texto na ordem contrária
        str -> str
    '''
    str.strip(texto,' ')
    minusc=str.lower(texto)
    novo=substitui(minusc)
    palavras=str.split(novo,' ')
    list.reverse(palavras)
    return ' '.join(palavras[1:])