def lingua_p(palavra):
    
    separada=[]
    indice=0
    
    while indice < len(palavra):
        list.append(separada,palavra[indice])
        indice=indice+1
    
    for letra in separada:
        
        if letra in "áaeéiíoóuú":
        
            posicao=list.index(separada,letra)
            separada[posicao]=letra+'p'+letra
            
    
    palavraP=str.join('',separada)
    
    return palavraP