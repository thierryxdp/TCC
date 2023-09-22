def lingua_p(palavra):
    '''Retorna uma palavra sendo alterada pela lingua do p
       parameter:
       palavra: palavra quaalquer a ser substituida
       str->str'''
    posicao=0
    str.lower(palavra)
    for vogal in palavra:
        if vogal in 'aáàãâéeêíiôoúu':
            texto=palavra.replace(vogal,vogal+'p'+vogal
            posicao+=1
            return texto