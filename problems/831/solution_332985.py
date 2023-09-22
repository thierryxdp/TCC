def lingua_p(palavra):
    '''funcao que traduz a palavra dada para a lingua do p, que coloca a letra p 
    após cada vogal, seguida pela vogal original; str -> str'''
    
    minusc = palavra.lower()
    
    nova_palavra = ''
    
    vogais = 'aeiouáéíóúãõàì'
    
    for p in minuscula:
        
        nova_palavra += p
        
        if p in vogais:
            
            palavra_nova += 'p' + p
            
    return palavra_nova