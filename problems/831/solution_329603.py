def lingua_p(palavra):
    '''
        dada um palavra em português retorna sua forma na língua do P.
        str -> str
    '''
    palavra.lower()
    P=''
    for el in palavra:
        if el in 'aeiouáâéêíôóú':
            P=P+el+'p'+el
        else:
            P=P+el
    return P