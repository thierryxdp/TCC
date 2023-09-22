def eh_quadrada(matriz):
    """Retorna true se uma matriz dada for quadrada
    e false se não for"""
    if len(matriz)>0:
        if len(matriz)==len(matriz[0]):
            return True
        else:
          return False
      else:
       return True