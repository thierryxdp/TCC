def lingua_p(palavra):
    """recebe uma palavra e retorna ela traduzida para a lingua do P
    string -> string"""
    
    palavra = str.lower(palavra)
    consoantes = ['q', 'w', 'r', 't', 'y', 'p', 's', 'd', 'f', 'g', 'h',
                  'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'ç']
    nova_palavra = ''
    
    for i in range(len(palavra)):
        if palavra[i] not in consoantes:
            nova_palavra += palavra[i] + 'p' + palavra[i]
            
        else:
            nova_palavra += palavra[i]
            
    return nova_palavra