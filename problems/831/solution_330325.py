def lingua_p(string):
    '''Função que transforma a string recebida em liguagem
    do p
    entrada=string
    saida=string'''
    x=''
    for h in string:
        if h in 'aeiouAEIOUúáéíó':
            x=x+h+'p'+ h
        else:
                x=x+ h
        
    return x