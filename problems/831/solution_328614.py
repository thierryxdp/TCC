def lingua_p(palavra):
    
    novapalavra = []
    palavra = palavra.lower()
    acumulador = 0
    
    for i in range(0,len(palavra)+1):
        
        exceto = "aáãâeéiíoóõôuú"
        
    	for i in palavra:
            
            if i in exceto:
                palavrap = i + "p" + i
                
                novapalavra.append(palavrap)
                
            else: 
                novapalavra.append(i)
                
        return list.join(novapalavra, "")