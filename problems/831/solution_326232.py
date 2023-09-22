def lingua_p(palavra):
    '''Retorna uma palavra sendo alterada pela lingua do p
       parameter:
       palavra: palavra quaalquer a ser substituida
       str->str'''
    str.lower(palavra)
    posicao=0
    while posicao < len(palavra):
        if palavra[posicao] in 'aeiouáàãêéíôú':
            posicao += 1
            texto=palavra.replace(palavra[posicao], palavra[posicao]+'p'+palavra[posicao],1)
    return texto