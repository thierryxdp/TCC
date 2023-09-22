def lingua_p(string):
    '''A função recebe uma palavra e
       retorna a mesma traduzida para
       a lingua do P;
       string -> string'''
    vogais = 'aeiouáéú'
    nova = string
    for i in range(len(string)):
        kaka = str.count(string,string[i])
        if kaka > 1 and string[i] in vogais: 
            nova = str.replace(nova,string[i],string[i]+'p'+string[i],kaka)
        if kaka == 1 and string[i] in vogais: 
            nova = str.replace(nova,string[i],string[i]+'p'+string[i],1)
    return nova