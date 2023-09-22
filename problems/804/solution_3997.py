#Start your python function here
def filtra_pares(x):

    tupla = []

  for i in range(3):
    if x[i]%2 == 0:
      tupla.append(x[i])
     

  return tuple(tupla)