def lingua_p(palavra):
    '''retorna uma palavra traduzida pela lingua do p
    str->str'''
    
    liguap=''
    for letra in palavra:
    	if letra in 'aeiou':
            linguap= letra+'p'+letra
        else:
            linguap=letra
    return linguap