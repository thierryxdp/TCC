def posLetra(frase,letra,num):
    quantidade_vezes=0
    i=0
    while i< len(frase):
        if frase[i] == letra :
            quantidade_vezes = quantidade_vezes + 1
        
        i=i+1
    return quantidade_vezes