def lingua_p(palavra:str)->str:
    """Dada uma palavra, retorna ela na língua do p, com p depois de toda vogal, seguida pela última vogal."""
    palavra_p=''
    for letra in palavra:
        if letra in 'aeiou':
            palavra_p=palavra_p+letra+'p'+letra
        elif letra in 'áéíóú':
            if letra=='á':
                palavra_p=palavra_p+letra+'pá'
            if letra=='é':
                palavra_p=palavra_p+letra+'pé'
            if letra=='í':
                palavra_p=palavra_p+letra+'pí'
            if letra=='ó':
                palavra_p=palavra_p+letra+'pó'
            if letra=='ú':
                palavra_p=palavra_p+letra+'pú'
        else:
            palavra_p= palavra_p+letra
    return str.lower(palavra_p)