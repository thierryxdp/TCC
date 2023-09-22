def lingua_p(palavra):
    '''Recebe uma palavra e retorna esta mesma 
    palavra traduzada para a lingua do P.
    string -> string'''
    palavra_p = ''
    
    for i in range(palavra):
        if i == ' ':
            palavra_p += ' '
        else:
            palavra_p += i
        return palavra_p