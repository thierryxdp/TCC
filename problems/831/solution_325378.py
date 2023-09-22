def lingua_p(palavra):
    
    palavra_m = str.lower(palavra)
    nova_palavra = ''
    
    for i in palavra_m:
        
        if i in 'aãáàeéiíoôóuú':
            nova_palavra += i + 'p' + i
            
        else:
            nova_palavra += i
            
    return nova_palavra