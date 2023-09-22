def filtra_Multiplos (x,n):
    if x%n==0:
       return True 
def fm(x,n):
   r=[]
   for e in x:
       if filtraMultiplos (e,n):
         r.append (e)
   return r