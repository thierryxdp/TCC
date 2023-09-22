def fatorial(n):
  if n > 0:
    fatorial = n
    i = n - 1
  
    while i > 0:
      fatorial = fatorial * i
      i = i - 1 
      
    return fatorial
  else:
    return 1