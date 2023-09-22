def freq_palavras(x):

    k ={}

    for i in x.split(' '):
        if i not in k:
            k[i] = 1 
            
        else:  
            k[i] += 1
            
    return k