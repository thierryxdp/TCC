def lingua_p(palavra):

    """ Nesta função, a cada vogal que aparece na string palavra fornecida, a
        função devolve a vogal mais a letra p mais a vogal mais uma vez.
        Caso seja uma consoante, nenhuma mudança é feita.
        str -> str
    """

    palavra_na_lingua_p = ''

    for letra in palavra:

        if letra in 'aeiouAEIOUãÃ':
            
            palavra_na_lingua_p = palavra_na_lingua_p + letra + 'p' + letra
            
        else:
            
            palavra_na_lingua_p = palavra_na_lingua_p + letra

    return str.lower(palavra_na_lingua_p)