def conta_frases(frase):
    interro = frase.count("?")
    exclam = frase.count("!")
    trespont = 0
    ponto = 0
    
    for i in range(len(frase)):
        if(frase[i] == "."):
            if(i < len(frase)-2):
                if(frase[i+1] == "."):
                    if(frase[i+2] == "."):
                		trespont+=1
                else:
                	ponto+=1
          	else:
                ponto+=1
            
    
    
    return interro + exclam + trespont + ponto