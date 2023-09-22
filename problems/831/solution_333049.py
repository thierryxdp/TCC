def lingua_p(palavra):
    '''Dado uma palavra em português, a função deve retornar 
    a palavra na lingua do p;
    str -> str'''
    
    vogais=['a','e','i','o','u']
    
    for i in palavra:
        p=str.lower(palavra)
        if i in vogais:
            p+='p'+p
            
    return (p)