def lingua_p(palavra):
    '''transforma uma palavra para sua forma na lingua do p
    adicionando um p onde tem vogal e repetindo ela em seguida
    str->str'''
    nova= '' 
    for l in palavra:
    	if l in 'aeiouáéúí':
            nova= nova + l + 'p' + l
        else: 
            nova=nova + l
    return nova