def bolos (a, b, c):
    """calcula o numero de bolos possiveis de serem confeccionados dados a quantidade a de xicaras
    de farinha de trigo, b de ovos e c de colheres de sopa de leite; int, int, int -> int"""
    if a//2>==b//3>==c//5 or b//3>==a//2>==c//5:
     return c//5
    elif b//2>==c//3>==a//2 or c//5>==b//3>==a//2:
      return a//2
    else:
      return b//3