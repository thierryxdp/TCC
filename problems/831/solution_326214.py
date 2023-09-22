def lingua_p(palavra):
    '''Retorna uma palavra sendo alterada pela lingua do p
       parameter:
       palavra: palavra quaalquer a ser substituida
       str->str'''
    str.lower(palavra)
    posicao=0
    for posicao in range(len(palavra)):
        vogal=palavra[posicao]
        if vogal in 'aáàãâéeêíiôoúu':
            palavra=palavra.replace(vogal,vogal+'p'+vogal,1)
    return palavra