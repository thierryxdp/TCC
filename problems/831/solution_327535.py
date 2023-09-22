def lingua_p(string):
    '''A função recebe uma palavra e
       retorna a mesma traduzida para
       a lingua do P;
       string -> string'''
    vogais = 'aeiou'
    for i in range(len(string)):
        if string[i]== vogais: 
            return i
    return i