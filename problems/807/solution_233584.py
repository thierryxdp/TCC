def conta_frases(texto): 
    
    cont1 = texto.split('.')
    cont2 = texto.split('!')
    cont3 = texto.split('?')
    cont4 = texto.count('...')
   
    return (len(cont1) - 2*cont4) + len(cont2) * 2