def freq_palavras(frases):
    """g"""
    frases.split(" ")

    a=frases
    
   
  
    dic={}
    
    for i in range(len(a)):
        
        b=int(frases.count(str(a[i])))
        
        dic.update({a[i]:b})
     
        
    return  dic