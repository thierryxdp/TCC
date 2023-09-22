def posLetra(stry,letra,num):
    """retorna a posicao que a ocorrencia da letra esta"""
    encontrar = str.find(stry,letra)
    
    contador=0
    
    while contador<len(stry):
        if letra in stry:
            oi = str.find(stry,letra,num,-1)
            contador+=1
        elif num < str.count(stry,letra)
        	oi = -1
            contador+=1
    return oi