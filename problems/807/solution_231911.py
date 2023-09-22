def conta_frases(abc):
          
       s1=str.split(abc,'.')
     
       s2=str.split(abc,'!',0)
      
       s3=str.split(abc,'-',0)
      
       s4=str.split(abc,'.',0)
      
       s5=str.split(abc,'...',0)
     
       return len(s1)+len(s2)+len(s3)+len(s4)+len(s5)