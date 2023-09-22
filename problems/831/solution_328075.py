def lingua_p(palavra):
    """função que receba uma palavra e retorne ela pala a língua do P; string->string"""
    l=''
    for i in palavra:
        if i in 'AEIOUÁÃÂÉÍÓÕÔÚaeiouáãâéíóõôú':
            l=l+'p'+l
    return l