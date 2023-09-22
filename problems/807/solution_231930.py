def conta_frases(abc):
          
       abc=str.split(abc,'...')
       abc=str.join(' ',abc)
       return len(str.split(abc,'.',0))