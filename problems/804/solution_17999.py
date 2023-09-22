#Start your python function here


def filtra_pares(x):
   Ordem = ()
   if x[0] %2 ==0:
       Ordem = Ordem + (x[0],)
   if x[1]%2==0:
        Ordem= Ordem + (x[1],)
   if x[2]%2==0:
        Ordem= Ordem + (x[2],)
   if x[3]%2==0:
        Ordem= Ordem + (x[3],)   
   return Ordem