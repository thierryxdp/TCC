def lingua_p(palavra):
    '''Dado uma palavra em português, a função deve retornar 
    a palavra na lingua do p;
    str -> str'''
    p=palavra.lower()
    vogais='a,e,i,o,u,á,é,í,ó,ú,ê,î,â,ô,û'
    
    for i in p:
        if i in vogais:
            p+='p'+p
            
    return (p)