def lingua_p(palavra):
    '''Recebe uma palavra e retorna esta mesma 
    palavra traduzada para a lingua do P.
    string -> string'''
    lingua_p = ''
    
    for i in palavra:
        if 'aeiou' in palavra:
            lingua_p = 'p' + i 
        return lingua_p