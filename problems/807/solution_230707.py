def conta_frases(texto):
    
    texto_2=str.replace(texto,"...",".")
    
    ponto_final=str.count(texto_2,".",len(texto))
    
    ponto_exclamacao:str.count(texto_2,"!",len(texto))
        
    ponto_interrogacao:str.count(texto_2,"?",len(texto))
        
    return ponto_final+ponto_exclamacao+ponto_interrogacao