def filtra_pares(x:tuple)->tuple:
     tuplaF = ()
     if x[0] % 2 == 0:
         tuplaF = tuplaF + (x[0],)  
     if x[1] % 2 == 0:
         tuplaF = tuplaF + (x[1],)
     if x[2] % 2 == 0:
         tuplaF = tuplaF + (x[2],)
     if x[3] % 2 == 0:
         tuplaF = tuplaF + (x[3],)
     return tuplaF