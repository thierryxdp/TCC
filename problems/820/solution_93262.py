def posLetra(frase,letra,num):
    lista=[frase]
    quantidade_vezes=0
    i=0
    while i< len(frase):
        if quantidade_vezes != num :
            quantidade_vezes = quantidade_vezes + 1
        
        i=i+str.find(frase,letra)
    return i