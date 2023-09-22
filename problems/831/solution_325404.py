def lingua_p(palavra):
    '''funcao que dado uma palavra a retorna na lingua de p
    str->str'''
    for i in 'aeiouéáú':
        palavra = str.replace(palavra, i, i+'p'+i)
    return palavra