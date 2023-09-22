def qtd_divisores(x):
    N = x
    for i in range(1, N + 1):
       if N% i == 0:
          return i