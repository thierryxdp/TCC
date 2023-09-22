def lingua_p(palavra):
    string=''
    
    for letra in palavra:
        if letra in 'AEIOUaeiouáãéíóú':
            string+=letra+'p'+letra
        else:
            string+=letra
    return  string