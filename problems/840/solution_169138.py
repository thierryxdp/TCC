def bolos(a = 2, b = 3, c = 5):
    x = a*b*c
    if(x == 30):
      return 1
    if(x > 30):
       return 2
    if(x == 0):
       return 0
    if( a < 2 && b < 3 && c < 5):
       return 0