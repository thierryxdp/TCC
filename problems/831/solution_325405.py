def lingua_p(texto):
    
    ''' Dando como entrada uma string, a funcao retorna a mesma palavra escri-
    ta em letra do p, ou seja, no formato vogal + 'p' + vogal;
    
    str -> str '''
    
    novoTexto = ''
    
    
    for elemento in range(len(texto)): 
        
        vogal = texto[elemento]
        
        if vogal in 'AEIOUÁÀÉÊÍÓÚáàéêíóúaeiou':
            
            novoTexto =  novoTexto + str.lower(texto[elemento]) + 'p' + str.lower(texto[elemento])
            
        else:
            
            novoTexto = novoTexto + str.lower(texto[elemento])
            
    return novoTexto