def substitui(s,x,i):
    """função que retorna uma palavra separada 
    por um caractere
    str,str,int -> str"""
   
    pt1 = s[0:i] 
    
    pt2 = s[i+1:len(s)] 

    return pt1 + x + pt2