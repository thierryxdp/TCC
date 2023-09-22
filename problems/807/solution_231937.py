def conta_frases(abc):
          
       t1=str.split(abc,'...')
       t2=str.join('~',t1)
       return len(str.split(t2,'~'))