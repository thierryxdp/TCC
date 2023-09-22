def lingua_p(palavra):
    '''Retorna uma palavra sendo alterada pela lingua do p
       parameter:
       palavra: palavra quaalquer a ser substituida
       str->str'''
    palavra=palavra.lower()
    palavra=list(palavra)
    texto=''
    posicao=0
    while posicao < len(palavra):
        vogal = palavra[posicao]
        if vogal in "aeiouáéíóúàèìòùâêîôûãõ":
            texto=texto+ vogal + "p" + vogal
            posicao=posicao+1
        else:
            texto=texto+vogal
            posicao=posicao+1
    return texto