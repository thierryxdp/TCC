def lingua_p(frase):
    lfrase = list(frase)
    pfrase = []
    for i in range(len(lfrase)):
        if lfrase[i] not in 'aeiouáéíóú':
            list.append(pfrase, lfrase[i])
        if lfrase[i] in 'aeiouáéíóú':
            list.append(pfrase, lfrase[i-1]+lfrase[i])
            list.append(pfrase, 'p'+lfrase[i])
            
        
       
            
    return str.join('',pfrase)