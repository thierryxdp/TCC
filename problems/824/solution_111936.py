def uppCons(frase):
    '''Recebe uma frase e retorna uma nova frase igual a 
       recebida porém com as consoantes maiúsculas;
       str -> str'''
    
    nova_frase = ''
    vogais = ['a','e','i','o','u','à','á','é','í','ó','ú','ã','â','ô']
    
    for n in frase:
        
        if n not in vogais:
            
            nova_frase += n.upper()
            
        elif n in vogais:
            
            nova_frase += n
            
    return nova_frase