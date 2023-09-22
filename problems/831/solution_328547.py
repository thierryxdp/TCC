def lingua_p(palavra):
    '''Traduz e retorna uma palavra dada por entrada para
       a língua do p, adicionando o p após cada vogal da
       palavra seguida da mesma vogal;
       str -> str'''
    
    minus = palavra.lower()
    
    vogais = ['a','e','i','o','u','á','é','í','ó','ú']
    
    trad = ''
    
    for n in minus:
        
        if n in vogais:
            
            trad += ''+n+'p'+n+''
            
        else:
            
            trad += n
            
    return trad