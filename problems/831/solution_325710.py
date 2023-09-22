def lingua_p(palavra:str)->str:
    """Dada uma palavra, retorna ela na língua do p, com p depois de toda vogal, seguida pela última vogal."""
    palavra_p=''
    for letra in palavra:
        if letra in 'aeiou':
            palavra_p=palavra_p+letra+'p'+letra
        if letra in 'áéíóú':
            elif letra='á':
                palavra_p=palavra_p+letra+'pa'
            elif letra='é':
                palavra_p=palavra_p+letra+'pe'
            elif letra='í':
                palavra_p=palavra_p+letra+'pi'
            elif letra='ó':
                palavra_p=palavra_p+letra+'po'
            elif letra='ú':
                palavra_p=palavra_p+letra+'pu'
        else:
            palavra_p= palavra_p+letra
    return str.lower(palavra_p)