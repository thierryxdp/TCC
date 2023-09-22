#Start your python function here
def filtra_pares(tup):
    """recebe tupla com 4 inteiros e retorna tupla apenas com os 
    valores pares da tupla original"""
  tup_pares=[elemento for elemento in tup if elemento %2 ==0]
  tup_filtrada = tuple(tup_pares)
  return tup_filtrada