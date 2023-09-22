def substitui_pontuacao1(f):
    f=str.replace(f,'... ',' ')
    f=str.replace(f,'? ',' ')
    f=str.replace(f,'. ',' ')
    f=str.replace(f,'- ',' ')
    f=str.replace(f,', ',' ')
    f=str.replace(f,'; ',' ')
    f=str.replace(f,': ',' ')
    f=str.replace(f,'! ',' ')
    return f
def inverte(frase):
    frase= substitui_pontuacao1(frase)
    frase=str.lower(frase)
    lista=str.split(frase,' ')
    lista[::-1]
    return str.join(' ',lista[::-1])