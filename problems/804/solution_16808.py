def filtra_pares(tupla):
    """recebe uma tupla com quatro elementos inteiros como parametro, e retorna uma nova tupla contendo apenas os elementos pares da tupla original"""
     final = ()
     if tupla[0] % 2 == 0:
         final += (tupla[0],)  
     if tupla[1] % 2 == 0:
         final += (tupla[1],)
     if tupla[2] % 2 == 0:
         final += (tupla[2],)
     if tupla[3] % 2 == 0:
         final += (tupla[3],)
     return final