def primo (x):
    """dado um numero inteiro positivo, a função responde se ele é ou não primo; 
    int -> bool"""
    for y in range(2,x):
      if x%y == 0:
        return False
    return True