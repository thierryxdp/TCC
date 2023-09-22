def posLetra(stry,letra,num):
    """retorna a posicao que a ocorrencia da letra esta"""
    encontrar = str.find(stry,letra)
    
    contador=0
    if num > str.count(stry,letra):
        return -1
    while contador<len(stry):
        if letra in stry:
            oi = str.find(stry,letra,num-1,-1)
            contador+=1
        if oi<num
        	oi = str.find(stry,letra,oi+1,-1)
            contador+=1
        else:
            contador+=1
        
    return oi