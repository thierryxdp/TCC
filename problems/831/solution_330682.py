def lingua_p(palavra):
    """ Função que recebe uma palavra e traduz ela
para a lingua do P. str -> str """
    
    nova_palavra = ''
    minsc = palavra.lower()
    
    for i in range(len(palavra)):
         
        if minsc[i] in "a":
             
            nova_palavra += minsc[i] +'pa'
            
        if minsc[i] in "e":
             
            nova_palavra += minsc[i] +'pe'
            
        if minsc[i] in "i":
             
            nova_palavra += minsc[i] +'pi'
            
        if minsc[i] in "o":
             
            nova_palavra += minsc[i] +'po'
            
        if minsc[i] in "u":
             
            nova_palavra += minsc[i] +'pu'
            
        if minsc[i] in "á":
             
            nova_palavra += minsc[i] +'pa'
            
        if minsc[i] in "é":
             
            nova_palavra += minsc[i] +'pe'
            
        if minsc[i] in "í":
             
            nova_palavra += minsc[i] +'pi'
            
        if minsc[i] in "ó":
             
            nova_palavra += minsc[i] +'po'
            
        if minsc[i] in "ú":
             
            nova_palavra += minsc[i] +'pu'
        

        if minsc[i] in "bcdfghjklmnpqrstvwxyz":
            nova_palavra += minsc[i]
      
            
    return nova_palavra