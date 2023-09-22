def uppCons(texto):
      i=0
      lista1=[]
      con=''
      while i<len(texto):
            if texto[i] in 'bcdfghjklmnpqrstvwyzç':
                  con=con+texto[i]
                  con=con.upper()
                  print(texto[i])
            if texto[i] in 'aeiouéóíáúâêîôû':
                  con=con+texto[i]
                  con=con.lower()
                  print(texto[i])
            
            i+=1
      return con