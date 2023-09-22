def lingua_p(palavra: str) -> str:
    
    a = str.split(palavra)
    vazio = []
    
    for letra in a:
        if "aeiou" == letra:
            vazio = vazio + letra + p
            
        else vazio += letra
        
	return vazio