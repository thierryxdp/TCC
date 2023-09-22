def posLetra(frase,letra,num):
    frase1= frase
    quantidade_vezes=0
    i=0
    while i< len(frase1):
        if frase[i] == letra:
            quantidade_vezes = quantidade_vezes +str.find(frase1,letra)
            frase1 = frase[str.find(frase1,letra)+1:]
            else:
                return -1
        i=i+1
    return quantidade_vezes