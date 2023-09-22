def lingua_p(palavra):
    '''Recebe uma palavra e retorna esta mesma 
    palavra traduzada para a lingua do P.
    string -> string'''
    
    palavra = palavra.lower()
    
    for i in palavra:
        if 'aeiou' in palavra:
            return True