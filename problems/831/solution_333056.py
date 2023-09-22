def lingua_p(palavra):
    '''Dado uma palavra em português, a função deve retornar 
    a palavra na lingua do p;
    str -> str'''
    p=palavra.lower()
    vogais='aeiouáéíóúêîâôû'
    palavra_do_p= ''
    
    for i in p:
        palavra_do_p=palavra_do_p+p
        if i in vogais:
            palavra_do_p+='p'+p
            
    return (palavra_do_p)