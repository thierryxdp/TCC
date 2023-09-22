def lingua_p(palavra):
    '''retorna uma palavra traduzida pela lingua do p
    str->str'''
    
    texto=''
    for letra in palavra:
        if letra in 'aeiou':
            texto+= letra+'p'+letra
        else:
            texto+= letra

        return texto