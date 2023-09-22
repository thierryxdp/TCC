def lingua_p(palavra):
    """ Função que traduz a palavra para a língua do P
    str -> str """
    x='AEIOUaeiou'
    i=0
    palavra_final=''
    while i<len(palavra):
        if palavra[i] in x:
            palavra_final=palavra[0:i]+'p'+palavra[i]
    return str.lower(palavra_final)