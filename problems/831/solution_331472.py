def lingua_p (frase):
    '''Retorna a frase traduzida para a língua do P. str->str'''
    fraseP=''
    for i in frase:
        if i in 'aeiouáàãâéêíîóôõúûÀAÃÂEÊÉIÍÔÕOÓUÚ':
            fraseP= fraseP+i+'p'+i
        else:
            fraseP= fraseP+i
    return fraseP