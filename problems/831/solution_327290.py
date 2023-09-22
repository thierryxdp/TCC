def lingua_p(palavra) : 
    
    """funcao que apos cada vogal de uma determinada palavra, adiciona 'p' e a vogal original"""
    #str -> str
    
    palavra = list(palavra.lower())
    aux = 0
    
    for i in palavra:
        if i in 'ãaáeéiouú':
        	a = 'p' + i 
        	palavra.insert(palavra.index(i, aux) + 1, a)
        	aux += 1

    novapalavra = ''.join(palavra)
    return novapalavra