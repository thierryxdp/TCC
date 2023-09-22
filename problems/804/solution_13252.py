def filtra_pares(s):
     return [n for n in s if n % 2 == 0]
    def check_even(number):
    if number % 2 == 0:
          return True  

    return False

# Extract elements from the numbers list for which check_even() returns True
filtro = filter(filtra_pares, s)

# converting to list
pares = list(filtro)