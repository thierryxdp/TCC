def lingua_p(palavra):
    '''Retorna uma palavra sendo alterada pela lingua do p
       parameter:
       palavra: palavra quaalquer a ser substituida
       str->str'''
    str.lower(palavra)
    for vogal in palavra:
        if vogal in 'aeiouáàãâéêíôú':
            palavra = palavra.replace(vogal,vogal+'p'+vogal)
            vogal = palavra[palavra.index(vogal)+2]
    return palavra