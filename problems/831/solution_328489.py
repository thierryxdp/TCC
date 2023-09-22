def lingua_p(frase):
    lfrase = list(frase)
    
    for i in range(len(lfrase)-1):
        if lfrase[i+1] in 'aeiou' and lfrase[i] not in 'aeiou':
            list.insert(lfrase, i+2, 'p'+lfrase[i+1])
         
    return str.join('',lfrase)