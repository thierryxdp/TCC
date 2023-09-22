def filtra_pares (t):
     '''Transforma uma tupla composta por números inteiros em uma tupla apenas com os números pares da anterior na mesma ordem;
     tuple -> tuple'''
     lista = t
     def par(p):
             if p % 2 == 0:
                     return True
             else:
                     return False
     return  tuple (filter(par,lista))