def lingua_p(palavra):
    '''Retorna a palavra traduzida para a língua do P'''
    '''str->str'''
    traduzida=''
    for x in palavra:
        if x in 'aeiou':
            traduzida=traduzida+x+'p'+x
        else:
            traduzida=traduzida+x
    return traduzida