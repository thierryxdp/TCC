def lingua_p(frase):
    lfrase = list(frase)
    
    for i in range(len(lfrase)):
        if lfrase[i] in 'aeiouáéíóú' and not i==len(frase)-1:
            list.insert(lfrase, i+1, 'p'+lfrase[i])
        if lfrase[i] in 'aeiouáéíóú' and i==len(frase)-1:
        	list.append(lfrase, 'p'+lfrase[i])
    return str.join('',lfrase)