def posLetra (string,letra,n):
    
    indice = 0
    poicao = str.find(string,letra)
    while indice < n -1:
        if letra in string:
            posicao = str.find(string,letra,posicao+1)
        indice = indice + 1 
    return posicao