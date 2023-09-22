def lingua_p(palavra):
    
    separada=[]
    indice=0
    
    while indice < len(palavra):
        list.append(separada,palavra[indice])
        indice=indice+1
    
    for letra in separada:
        
        if letra in "aeiou":
            posicao=list.index(separada,letra)
            list.insert(separada,posicao,'p'+letra)
    
    palavraP=str.join('',separada)
    
    return palavraP