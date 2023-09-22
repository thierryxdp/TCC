def lingua_p(palavra):
    '''Retorna uma palavra sendo alterada pela lingua do p
       parameter:
       palavra: palavra quaalquer a ser substituida
       str->str'''
    posicao=0
    str.lower(palavra)
    for vogal in palavra:
        if vogal in 'aeiouáàãâéêíôú':
            palavra = palavra.replace(vogal,vogal+'p'+vogal,1)
            vogal = palavra[posicao]
            posicao+=0
    return palavra