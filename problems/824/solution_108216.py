def uppCons(frase):
    i=0
    string = str("")
    while i<len(frase):
        
        if frase[i] in "AEIOUaeiou":
            string = string + frase[i]
            
        else:
            string = string + frase[i].upper
            
        i=i+1
            
    return string