def lingua_p(string):
    '''A função recebe uma palavra e
       retorna a mesma traduzida para
       a lingua do P;
       string -> string'''
    vogais = 'aeiouáé'
    nova = ''
    for i in range(len(string)):
        if string[i] in vogais: 
            nova = str.replace(string,string[i],string[i]+'p'+string[i])
    return nova