def conta_frases(texto):
    
    
     frase1=[str.split(texto,'.')] 
     frase2=[str.split(texto,'?')]+frase1
     frase3=[str.split(texto,'!')]+frase1+frase2
     frase4=[str.split(texto,'...')]+frase1+frase2+frase3
            
    
    return len(frase4)