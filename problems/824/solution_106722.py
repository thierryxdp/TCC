def uppCons(frase):
    ''' Dada como entrada uma frase, a funcao retorna a mesma frase, porem
    com todas as consoantes em letra maiuscula;
    
    str -> str '''
    
    fraseNova = frase
    elemento = 0
    
    while elemento < len(frase):
        
        if frase[elemento] not in 'AEIOUaeiouáàéíóúã':
            fraseNova = (str.replace(fraseNova,fraseNova[elemento],str.upper(fraseNova[elemento])))
                         
        elemento = elemento + 1
        
    return fraseNova