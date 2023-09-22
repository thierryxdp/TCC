def lingua_p(palavra):
    '''Dado uma palavra em português, a função deve retornar 
    a palavra na lingua do p;
    str -> str'''
    p=str.lower(palavra)
    vogais=['a','e','i','o','u']
    
    for i in p:
        m=str.index(p,i)
        if m in list.index(vogais):
            p=str.join('p',p)
            
    return (p)