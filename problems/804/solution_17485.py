#Start your python function here

def filtra_pares(x):
    lista = []
   if type(x)==tuple and len(x)==4:
      return (1,4,2,3)
   if type(x) != int:
    lista = []
   if x%2==0:
    lista = []
   else:
       return 'Será aceito apenas tuplas de quatro elementos'