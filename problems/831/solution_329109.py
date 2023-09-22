def lingua_p(palavra): 
    P=''
    for letra in palavra: 
        P+= letra
        if letra in 'aeiouAEIOU' :
            P+= 'p'+letra 
    return P