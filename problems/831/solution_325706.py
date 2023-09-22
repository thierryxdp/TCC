def lingua_p(palavra:str)->str:
    """Dada uma palavra, retorna ela na língua do p, com p depois de toda vogal, seguida pela última vogal."""
    palavra_p=''
    for letra in palavra:
        if letra in 'aeiou':
            palavra_p=palavra_p+letra+'p'+letra
        else:
            palavra_p= palavra_p+letra
    return str.lower(palavra_p)