#Funcao que recebe uma tupla com quatro elementos int como parametro e retorna uma nova tupla

# int, int, int, int -> tupla 
def filtra_pares(x):
   if x%2==0:
      return 'Aceito apenas se for int e par'
  elif x!=int:
      return 'A tupla deve apenas conter elementos int'
  else:
      return 'Será aceito apenas uma tupla com quatro elementos int'