def primo (x):
     if (x > 1):
          for i in range (2, x + 1):
               if (x%i == 0 and i != x and i != 1):
                    return False
          else:
               return True
     else:
          return False