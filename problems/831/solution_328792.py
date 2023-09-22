novapalavra = []
    palavra = palavra.lower()
    
  
        
    exceto = "aáãâeéiíoóõôuú"

    for i in palavra:
        if i in exceto:
            palavrap = i + "p" + i
            novapalavra.append(palavrap)
        else: 
            novapalavra.append(i)
                
    return "".join(novapalavra)