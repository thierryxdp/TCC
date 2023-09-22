def conta_frases(texto):
    """Dado um texto retorna a quantidade frases. str -> int """
    
    pontuacao = 0
    if texto.find("."):
        
        pontuacao +=1
        
    if texto.find("!"):
        
        pontuacao +=1
        
    if texto.find("?"):
        
        pontuacao +=1
        
    if texto.find("..."):
        
        pontuacao +=1
        
        return pontuacao