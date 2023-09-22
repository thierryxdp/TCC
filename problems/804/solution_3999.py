#Start your python function here
def filtra_pares(x):

    tupla = []

  for i in range(len(x)):
    if x[i]%2 == 0:
      tupla.append(x[i])
     
  return tuple(tupla)