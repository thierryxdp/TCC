def lingua_p(palavra):
    """ Função que traduz a palavra para a língua do P
    str -> str """
    x='AEIOUaeiou'
    i=0
    palavra_final=''
    while i<len(palavra):
        if palavra[i] in x:
            palavra[i+1]='p'
            palavra[i+2]=palavra[i]
    return str.lower(palavra)