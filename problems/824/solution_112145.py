def uppCons(frase):
    
    
    a=str.upper(frase)
    
    vogal=['a','e','i','o','u']
    fpartida= str.split(a)
    
    matriz = [list(palavra) for palavra in fpartida ]
    
    for i in matriz:
        for j in matriz:
            if j in vogal:
                j=str.lower(j)
                
               
                
    
  
    
    
    
    
    return matriz