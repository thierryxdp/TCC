def filtra_pares(g):
    ''' funcao que recebe 4 tuplas e retorna apeas os elementos paraes; g= int'''
 


filtra= ()
   if g[0]%2==0:
       filtra = filtra +(g[0],)
   if g[1]%2==0:
       filtra =filtra +(g[1],)
   if g[2]%2==0:
       filtra = filtra +(g[2],)
   if g[3]%2==0:
       filtra = filtra +(g[3],)
   return filtra