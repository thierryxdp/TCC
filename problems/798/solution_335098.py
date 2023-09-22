def freq_palavras(frases):
    """g"""
    a=frases.split(" ")
   
    
   
  
    dic={}
    
    for i in range(len(a)):
        
        b=int(frases.count(str(a[i])))
        
        dic.update({a[i]:b})
     
        
    return  dic