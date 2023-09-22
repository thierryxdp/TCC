def lingua_p(palavra): 
    P=''
    for letra in palavra: 
        p+= letra
        if letra == 'aeiouAEIOU' :
            P+= 'p'+letra 
    return P