def conta_frases(texto_x):
    
    #Computando o número de frases que acabam com ".":
    n_ponto = int(str.count(texto_x, "."))
    
    #Computando o número de frases que acabam com "?":
    n_inte = int(str.count(texto_x, "?"))
    
    #Computando o número de frases que acabam com "!":
    n_excl = int(str.count(texto_x, "!"))
    
    #Computando o número de frases que acabam com "…":
    n_3pontos = int(str.count(texto_x, "..."))
    
    #Calculando o número final de frases:
    numero_final_de_frases = n_ponto + n_inte +  n_excl + n_3pontos  
    
    #Retornando:
    return numero_final_de_frases