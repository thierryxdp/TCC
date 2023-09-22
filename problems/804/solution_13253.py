def filtra_pares(s):

    def check_even(number):
    if number % 2 == 0:
          return True  

    return False

# Extract elements from the numbers list for which check_even() returns True
filtro = filter(filtra_pares, s)

# converting to list
 return pares = list(filtro)