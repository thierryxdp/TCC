#Start youdef filtra_pares(x, y, w, z)->tuple:
def filtra_pares(x, y, w, z)->tuple:
     final = ()
     if x % 2 == 0:
         final += (tuple[x],)  
     if y % 2 == 0:
         final += (tuple[y],)
     if w % 2 == 0:
         final += (tuple[w],)
     if z % 2 == 0:
         final += (tuple[z],)
     return final