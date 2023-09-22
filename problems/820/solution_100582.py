def posLetra(str,letra,num):
    """retorna a posicao que a ocorrencia da letra esta"""
    encontrar = str.find(str,letra)
    
    contador=0
    
    while contador<len(str):
        if letra in str:
            oi = str.find(str,letra,contador)
            contador+=1
        else:
            contador+=1
            
    return oi