def lingua_p(palavra):
    '''retorna uma palavra traduzida pela lingua do p
    str->str'''
    
    frase=''
    for letra in palavra:
    	if letra in 'aeiou':
            frase= letra+'p'+letra
        else:
            frase=letra
    return frase