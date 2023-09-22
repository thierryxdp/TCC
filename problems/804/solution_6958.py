def filtra_pares(tup):
  tup_pares=[elemento for elemento in tup if elemento %2 ==0]
  tup_filtrada = tuple(tup_pares)
  return tup_filtrada