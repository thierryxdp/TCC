def posLetra(f,l,n):
    ''''''
    ''''''
    
    pos = 0
    rep = 0
    
    while pos < len(f):
          
          if f[pos] == l:
                rep = rep + 1
                
                if rep == n:
                    return pos 
         
          pos = pos + 1
    return -1