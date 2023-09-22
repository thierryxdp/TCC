def uppCons(frase):
    i=0
    consoantes="BCÇDFGHJKLMNPQRSTVWXYZbcçdfghjklmnpqrstvwxyz"
    string=""
    while i< len(frase):
        if frase[i] in consoantes:
            string += frase[i].upper 
        else: 
            string += frase[i]
        i+=1
    return string