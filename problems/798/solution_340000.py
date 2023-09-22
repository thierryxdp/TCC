def freq_palavras(frases): 
    
    if frases[-1] == '.': 
        frases = frases[0:len(frase) - 1] 
   
    
    
    elif frases in dictionary: 
        dictionary[frases] += 1
   
    
    
    else: 
        dictionary.update({frases: 1}) 
   
   
dictionary = {} 
   
lst = frases.split() 
   
for frases in lst: 
return dictionary