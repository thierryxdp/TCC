def lingua_p(palavra):
    '''Dado uma palavra em português, a função deve retornar 
    a palavra na lingua do p;
    str -> str'''
    p=str.lower(palavra)
    vogais='aeiouáéíóúêîâôûã'
    palavra_do_p= ''
    
    for i in p:
        palavra_do_p=palavra_do_p+i
        if i in vogais:
            palavra_do_p=palavra_do_p+'p'+i
            
    return (palavra_do_p)