def eh_quadrada(M):
    if len(M) == 0:
     return True
elif len(M) > 0:
     if len(M) == len(M[0]):
          return True
     else:
          return False
else: 
     print("len não pode ser negativo")