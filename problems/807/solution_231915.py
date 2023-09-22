def conta_frases(abc):
          
       s1=str.split(abc,'. ')
     
       s2=str.split(abc,'!',0)
      
       s3=str.split(abc,'-',0)
                  
       s5=str.split(abc,'...',0)
     
       return len(s1)-1+len(s2)-1+len(s3)-1+len(s5)-1