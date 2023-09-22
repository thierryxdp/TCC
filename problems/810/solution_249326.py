def inverte(frase):
    '''str->str
    função que remove qualquer pontuação e substitui por espaço, transforma todas em minusculo e inverte a frase'''
    lista=str.split(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase, '.',' '),'?',' '),'!',' '),'...',' '),'   ',' '),'-',' '),',',' '),':',' '),';',' '))
    list.reverse(lista)
    return str.lower(str.join(' ',lista))