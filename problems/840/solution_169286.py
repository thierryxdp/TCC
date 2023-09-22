def bolos(a = 2, b = 3, c = 5):
    y = a/2
    x = b/3
    z = c/5
    if y*x*z == 0 :
      return 0
    if y < 1 or x < 1 or z < 1 :
      return 0
    if x*y*z == 1:
      return 1
    if(x*y*z == 8):
      return 2
    if x*y*z > 8:
      return 3