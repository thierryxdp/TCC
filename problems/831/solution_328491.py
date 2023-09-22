def lingua_p(frase):
    lfrase = list(frase)
    
    for i in range(len(lfrase)):
        if lfrase[i] in 'aeiou':
            list.insert(lfrase, i+1, 'p'+lfrase[i])
         
    return str.join('',lfrase)