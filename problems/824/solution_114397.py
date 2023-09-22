def uppCons(frase):
    """recebe uma frase e retorna a frase com as consoantes em maiusculo"""
    fraseedit = ''
    contador = 0
    
    while contador<len(frase):
        if str.lower(frase[contador]) in "bcdfghjklmnpqrstwxyzç":
        	maiusculo = str.upper(frase[contador])
        	fraseedit+= maiusculo
        	contador+=1
        
        elif str.lower(frase[contador]) in "aeiouàèìòùáéíóúãõ":
        	minusculo = frase[contador]
        	fraseedit+= minusculo
            contador+=1
        
    return fraseedit