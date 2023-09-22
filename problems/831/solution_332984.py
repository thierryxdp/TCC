def lingua_p(palavra):
    '''funcao que traduz a palavra inserida para a lingua do p, que adiciona a letra p apos cada vogal, seguida pela vogal original str->str'''
    
    minuscula = palavra.lower()
    
    palavra_nova = ''
    
    vogais = 'aeiouáéíóúãõàì'
    
    for p in minuscula:
        
        palavra_nova += p
        
        if p in vogais:
            
            palavra_nova += 'p' + p
            
    return palavra_nova