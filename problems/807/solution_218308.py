def conta_frases(frase):
    
    sinais=["!","?"]     
            
    pontuacao= str.split(frase,sinais)    
        
   
    return len(pontuacao)