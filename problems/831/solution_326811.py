def lingua_p(palavra):
    '''
    Função que revebe uma str em português e retorna e mesma traduzida 
    para linguagem do p
    '''
    vowels = "AaEeIiOoUuÉéÁáÚúÓóÍí"
    final=''
    for each in palavra:
        if each in vowels:
            final+=each+'p'+each
        else:
            final+=each
    return final